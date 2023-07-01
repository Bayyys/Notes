package com.bayyy.servlet;

import javax.servlet.ServletException;
import javax.servlet.ServletOutputStream;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.FileInputStream;
import java.io.IOException;
import java.net.URLEncoder;

public class FileServlet extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        System.out.println("进入了FileServlet");
        // 1.要获取下载文件的路径
        String realPath = "D:\\Coding\\test\\temp\\JavaWeb\\javaweb-02-servlet\\response\\src\\main\\resources\\img.png";
        System.out.println("下载文件的路径：" + realPath);
        // 2.下载的文件名是啥？
        String fileName = realPath.substring(realPath.lastIndexOf("\\") + 1);
        // 3.设置想办法让浏览器能够支持(Content-Disposition)下载我们需要的东西
//        resp.setHeader("Content-Disposition", "attachment;filename=" + fileName);    // Content-Disposition是响应头，attachment是附件，filename是文件名
        resp.setHeader("Content-Disposition", "inline;filename=" + URLEncoder.encode(fileName, "UTF-8"));    // inline是在线打开，attachment是附件，filename是文件名，URLEncoder.encode是编码转换(实现中文路径)
        // 4.获取下载文件的输入流
        FileInputStream in = new FileInputStream(realPath);
        // 5.创建缓冲区
        int len = 0;
        byte[] buffer = new byte[1024];
        // 6.获取OutputStream对象
        ServletOutputStream out = resp.getOutputStream();
        // 7.将FileOutputStream流写入到buffer缓冲区，使用OutputStream将缓冲区中的数据输出到客户端
        while ((len = in.read(buffer)) > 0) {
            out.write(buffer, 0, len);
        }
        // 8.关闭流
        out.close();
        in.close();
    }

    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        doGet(req, resp);
    }
}
