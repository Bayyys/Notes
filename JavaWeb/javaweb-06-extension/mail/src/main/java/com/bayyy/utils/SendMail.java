package com.bayyy.utils;

import com.bayyy.pojo.User;
import com.sun.mail.util.MailSSLSocketFactory;

import javax.mail.*;
import javax.mail.internet.InternetAddress;
import javax.mail.internet.MimeMessage;
import java.util.Properties;

/*
网站3秒原则：用户体验

让用户不等待，事情也还做？
用户执行完这个方法，它还走它的东西，我走我的页面
通过多线程，实现用户体验！（异步处理）

 */
public class SendMail extends Thread {


    // 用于给用户发送邮件的邮箱
    private String from = "475417309@qq.com";
    // 邮箱的用户名
    private String username = "bayyy";
    // 邮箱的密码
    private String password = "jgzstcpgefazbjbg";
    // 发送邮件的服务器地址
    private String host = "smtp.qq.com";

    // 导入一个类
    private User user;

    public SendMail(User user) {
        this.user = user;
    }


    @Override
    public void run() {

        try {
            Properties prop = new Properties();

            prop.setProperty("mail.host", host);///设置QQ邮件服务器
            prop.setProperty("mail.transport.protocol", "smtp");///邮件发送协议
            prop.setProperty("mail.smtp.auth", "true");//需要验证用户密码
            // QQ邮箱需要设置SSL加密
            MailSSLSocketFactory sf = new MailSSLSocketFactory();
            sf.setTrustAllHosts(true);
            prop.put("mail.smtp.ssl.enable", "true");
            prop.put("mail.smtp.ssl.socketFactory", sf);

            // 使用javaMail发送邮件的5个步骤

            // 1.创建定义整个应用程序所需要的环境信息的session对象
            Session session = Session.getDefaultInstance(prop, new Authenticator() {
                @Override
                protected PasswordAuthentication getPasswordAuthentication() {
                    return new PasswordAuthentication(from, password);
                }
            });
            // 开启session的debug模式，这样可以查看到程序发送Email的运行状态
            session.setDebug(true);

            // 2.通过session得到transport对象
            Transport ts = session.getTransport();

            // 3.使用邮箱的用户名和授权码连上邮件服务器
            ts.connect(host, username, password);

            // 4.创建邮件：写文件

            // 注意需要传递session
            MimeMessage message = new MimeMessage(session);
            // 指明邮件的发件人
            message.setFrom(new InternetAddress(from));
            // 指明邮件的收件人
            message.setRecipient(Message.RecipientType.TO, new InternetAddress(user.getEmail()));   // 从前端接收的
            // 邮件标题
            message.setSubject("注册通知");
            // 邮件的文本内容

            String info = "恭喜你(" + user.getUsername() + ")成功注册！" + "密码：" + user.getPassword();
            message.setContent(info, "text/html;charset=UTF-8");
            message.saveChanges();//保存更改

            // 5.发送邮件
            ts.sendMessage(message, message.getAllRecipients());

            // 6.关闭连接
            ts.close();
        } catch (Exception e) {
            System.out.println(e);
        }
    }
}
