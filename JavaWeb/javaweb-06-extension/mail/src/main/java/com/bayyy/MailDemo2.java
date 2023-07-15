package com.bayyy;

import com.sun.mail.util.MailSSLSocketFactory;

import javax.activation.DataHandler;
import javax.activation.FileDataSource;
import javax.mail.*;
import javax.mail.internet.InternetAddress;
import javax.mail.internet.MimeBodyPart;
import javax.mail.internet.MimeMessage;
import javax.mail.internet.MimeMultipart;
import java.util.Properties;

public class MailDemo2 {
    public static void main(String[] args) throws Exception {
        // 打印当前路径
        System.out.println(System.getProperty("user.dir"));
        //Properties中 设置属性
        Properties prop = new Properties();
        prop.setProperty("mail.host", "smtp.qq.com");///设置QQ邮件服务器
        prop.setProperty("mail.transport.protocol", "smtp");///邮件发送协议
        prop.setProperty("mail.smtp.auth", "true");//需要验证用户密码

        //QQ邮箱需要设置SSL加密，原因：大厂。其他邮箱不需要
        MailSSLSocketFactory sf = new MailSSLSocketFactory();
        sf.setTrustAllHosts(true);
        prop.put("mail.smtp.ssl.enable", "true");//使用安全的连接为true
        prop.put("mail.smtp.ssl.socketFactory", sf);//socket工厂，使用自己的socket工厂

        //使用javaMail发送邮件的5个步骤
        //1.创建定义整个应用程序所需要的环境信息的session对象

        //QQ才有!其他邮箱就不用
        Session session = Session.getDefaultInstance(prop, new Authenticator() {//获取默认的实例
            @Override
            protected PasswordAuthentication getPasswordAuthentication() {
                //发件人邮箱、授权码
                return new PasswordAuthentication("475417309@qq.com", "jgzstcpgefazbjbg");
            }
        });

        //开启session的debug模式，这样可以查看到程序发送Email的运行状态
        session.setDebug(true);

        //2.通过session得到transport对象
        Transport ts = session.getTransport();

        //3.使用邮箱的用户名和授权码连上邮件服务器
        ts.connect("smtp.qq.com", "475417309@qq.com", "jgzstcpgefazbjbg");

        //4.创建邮件：写邮件
        //需要传递session
        MimeMessage message = new MimeMessage(session);

        //指明邮件的发件人
        message.setFrom(new InternetAddress("475417309@qq.com"));

        //指明邮件的收件人，现在发件人和收件人是一样的，那就是自己给自己发
        message.setRecipient(Message.RecipientType.TO, new InternetAddress("475417309@qq.com"));

        //邮件的标题   只包含文本的简单邮件
        message.setSubject("发送的标题");

        //邮件的文本内容
        message.setContent("你好", "text/html;charset=UTF-8");

        /* ================== 图片和附件的邮件 ================== */
        /* ================== 准备图片数据 ================== */
        MimeBodyPart image = new MimeBodyPart();
        //图片需要经过数据化的处理  DataHandler：数据处理    FileDataSource：加载文件的资源
        DataHandler dh = new DataHandler(new FileDataSource("D:\\Coding\\test\\temp\\JavaWeb\\javaweb-06-extension\\mail\\src\\main\\resources\\girl.jpg"));
        //在body中放入这个处理的图片数据
        image.setDataHandler(dh);
        //给这个body设置一个ID名字
        image.setContentID("girl.jpg");

        /* ================== 准备正文数据 ================== */
        MimeBodyPart text = new MimeBodyPart();
        text.setContent("这是一张正文<img src='cid:girl.jpg'>", "text/html;charset=UTF-8");

        /* ================== 准备附件数据 ================== */
        MimeBodyPart body1 = new MimeBodyPart();
        body1.setDataHandler(new DataHandler(new FileDataSource("D:\\Coding\\test\\temp\\JavaWeb\\javaweb-06-extension\\mail\\src\\main\\resources\\watermelon.jpg")));
        body1.setFileName("1.txt");

        //描述数据关系
        MimeMultipart mm = new MimeMultipart();
        mm.addBodyPart(body1);
        mm.addBodyPart(text);
        mm.addBodyPart(image);
        mm.setSubType("mixed");

        //设置到消息中，保存修改
        message.setContent(mm);
        message.saveChanges();

        /* ================== 图片和附件的邮件准备结束 ================== */

        //5.发送邮件
        ts.sendMessage(message, message.getAllRecipients());

        //6.关闭连接，一切网络都需要关闭
        ts.close();
    }
}
