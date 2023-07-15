package com.bayyy.servlet;

import org.apache.commons.fileupload.FileItem;
import org.apache.commons.fileupload.FileUploadException;
import org.apache.commons.fileupload.ProgressListener;
import org.apache.commons.fileupload.disk.DiskFileItemFactory;
import org.apache.commons.fileupload.servlet.ServletFileUpload;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.util.List;
import java.util.UUID;

public class FileServlet extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        System.out.println("========== 进入 FileServlet ==========");
        // 1. 判断上传的文件是普通表单还是带文件的表单
        if (!ServletFileUpload.isMultipartContent(req)) {
            System.out.println("进入了 普通表单");
            return; // 终止方法运行，说明这是一个普通的表单，直接返回
        }

        // 2. 文件存储空间创建
        // 创建上传文件的保存路径，建议在 WEB-INF 路径下，安全，用户无法直接访问上传的文件
        System.out.println("带文件的表单");
        String uploadPath = this.getServletContext().getRealPath("/WEB-INF/upload");    // 获取上传文件存储目录文件名, 不存在就创建
        File uploadDir = new File(uploadPath);
        if (!uploadDir.exists()) {
            uploadDir.mkdir(); // 没有这个目录就创建这个目录
        }

        // 3. 缓存存储空间创建(缓存，临时文件)
        // 临时路径，假如文件超过了预期的大小，我们就把它放到一个临时文件中，过几天自动删除，或者提醒用户转存为永久
        String tmpPath = this.getServletContext().getRealPath("/WEB-INF/tmp");    // 获取临时文件存储目录文件名, 不存在就创建
        File tmpDir = new File(tmpPath);
        if (!tmpDir.exists()) {
            tmpDir.mkdir(); // 没有这个目录就创建这个目录
        }

        // 处理上传的文件，一般都需要通过流来获取，我们可以使用 request.getInputStream() 来获取请求的正文内容, 原生态的文件上传流获取请求的正文内容, 但是用起来比较麻烦
        // * 建议使用 Apache 的文件上传组件来实现，common-fileupload, 它需要依赖于 commons-io 组件
        String msg = "文件上传失败";
        try {
            // 1. 创建 DiskFileItemFactory 对象，处理文件上传路径或者大小限制的
            DiskFileItemFactory factory = getDiskFileItemFactory(tmpDir);
            // 2. 获取 ServletFileUpload
            ServletFileUpload upload = getServletFileUpload(factory);
            // 3. 处理上传的文件
            msg = uploadParseRequest(upload, req, uploadPath);
        } catch (FileUploadException e) {
            throw new RuntimeException(e);
        }

        // 4. 返回信息
        req.setAttribute("msg", msg);
        req.getRequestDispatcher("info.jsp").forward(req, resp);
    }

    public DiskFileItemFactory getDiskFileItemFactory(File tempDir) {
        DiskFileItemFactory factory = new DiskFileItemFactory();
        // 通过这个工厂设置一个缓冲区，当上传的文件大小超过这个缓冲区的时候，就会生成一个临时文件存放到指定的临时目录中
        factory.setSizeThreshold(1024 * 1024); // 缓冲区大小为 1M
        factory.setRepository(tempDir); // 设置临时目录
        return factory;
    }

    public static ServletFileUpload getServletFileUpload(DiskFileItemFactory factory) {
        ServletFileUpload upload = new ServletFileUpload(factory);
        // 监听文件上传进度
        upload.setProgressListener(new ProgressListener() {
            @Override
            // pBytesRead: 已经读取到的文件大小
            // pContentLength: 文件大小
            public void update(long pBytesRead, long pContentLength, int PItems) {
                System.out.println("总大小: " + pContentLength + " 已上传: " + pBytesRead);
            }
        });

        // 处理乱码问题
        upload.setHeaderEncoding("UTF-8");
        // 设置单个文件的最大值
        upload.setFileSizeMax(1024 * 1024 * 10);
        // 设置总共能够上传文件的大小
        // 1024 = 1kb * 1024 = 1M * 10 = 10M
        upload.setSizeMax(1024 * 1024 * 10);
        return upload;
    }

    public static String uploadParseRequest(ServletFileUpload upload, HttpServletRequest req, String uploadPath) throws FileUploadException, IOException {
        String msg = "文件上传失败";

        // 1. 解析前端请求，封装成一个 FileItem 对象
        List<FileItem> fileItems = upload.parseRequest(req);    // 使用文件解析对象的 parseRequest(req) 方法解析 request 对象，会将前端表单封装成一个个 FileItem 对象，然后放入到一个 List 中
        // 循环判断，每一个表单项，是普通类型，还是上传的文件
        for (FileItem fileItem : fileItems) {
            // 判断上传的文件是普通的表单还是带文件的表单
            if (fileItem.isFormField()) {
                // 为 true，表示这是一个普通的表单项
                // getFieldName 拿到的是前端表单控件的 name
                String name = fileItem.getFieldName();  // 获取非文件<input>表单项的 name 属性值
                String value = fileItem.getString("UTF-8"); // 获取非文件<input>标签的value内容
                System.out.println(name + ": " + value);
            } else {
                // 判断其为上传的文件
                /* ========== 处理文件 ========== */

                // 拿到文件名
                String uploadFileName = fileItem.getName();
                System.out.println("上传的文件名: " + uploadFileName);

                if (uploadFileName.trim().equals("") || uploadFileName == null) {   // 如果上传的文件名为空，即没有上传文件
                    continue;   // 跳过本次循环
                }

                // 获得上传的文件名 /img/date/this.png
                String fileName = uploadFileName.substring(uploadFileName.lastIndexOf("/") + 1);
                // 获得文件的后缀名
                String fileExtName = uploadFileName.substring(uploadFileName.lastIndexOf(".") + 1);

                System.out.println("文件信息 [文件名: " + fileName + " ---文件类型: " + fileExtName);

                // 可以使用 UUID(唯一识别的通用码), 保证文件名唯一
                // UUID.randomUUID().toString() 生成随机数
                String uuidPath = UUID.randomUUID().toString();

                /* ========== 文件处理完毕 ========== */

                // 存到哪? uploadPath
                // 文件真实存在的路径 realPath = uploadPath + "/" + uuidPath = /WEB-INF/upload/uuidPath
                String realPath = uploadPath + "/" + uuidPath;  // 文件存储文件夹的真实路径 String
                // 给每个文件创建一个对应的文件夹
                File realFilePath = new File(realPath); // 文件存储文件夹的真实路径 File
                if (!realFilePath.exists()) {
                    realFilePath.mkdir();   // 创建文件夹(一般都是不存在的)
                }

                /* ========== 存放地址 ========== */
                InputStream is = null;

                // 获取文件上传的流
                try {
                    is = fileItem.getInputStream();
                } catch (IOException e) {
                    e.printStackTrace();
                }

                // 创建一个文件输出流
                // realPath = 真实的文件夹
                // 差了一个文件; 加上输出文件的名字 + "/" + uuidFileName
                FileOutputStream fos = new FileOutputStream(realPath + "/" + fileName);

                // 创建一个缓冲区
                byte[] buffer = new byte[1024 * 1024];

                // 判断是否读取完毕
                int len = 0;
                // 如果大于 0 说明还存在数据
                while ((len = is.read(buffer)) > 0) {
                    fos.write(buffer, 0, len);  // 输出文件(将文件流写入 realPath + "/" + uuidFileName)
                }

                // 关闭流
                fos.close();
                is.close();

                msg = "文件上传成功";
                fileItem.delete();  // 上传成功，清除临时文件
            }
        }
        return msg;
    }

    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        doGet(req, resp);
    }
}
