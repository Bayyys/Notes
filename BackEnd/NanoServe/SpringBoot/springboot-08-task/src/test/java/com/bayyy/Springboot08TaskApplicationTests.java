package com.bayyy;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.mail.SimpleMailMessage;
import org.springframework.mail.javamail.JavaMailSender;
import org.springframework.mail.javamail.JavaMailSenderImpl;
import org.springframework.mail.javamail.MimeMessageHelper;

import javax.mail.MessagingException;
import javax.mail.internet.MimeMessage;
import java.io.File;

@SpringBootTest
class Springboot08TaskApplicationTests {
    @Autowired
    JavaMailSenderImpl mailSender;

    @Test
    void SimpleMail() {
        // 简单邮件
        SimpleMailMessage message = new SimpleMailMessage();
        message.setSubject("简单邮件测试");
        message.setText("这是一封简单邮件");
        message.setTo("475417309@qq.com");
        message.setFrom("475417309@qq.com");
        mailSender.send(message);
    }

    @Test
    void ComplexMail() throws MessagingException {
        MimeMessage mimeMessage = mailSender.createMimeMessage();
        MimeMessageHelper helper = new MimeMessageHelper(mimeMessage, true);

        helper.setSubject("复杂邮件测试");
        // 第二个参数为true表示开启HTML
        helper.setText("<p style='color:red'>这是一封复杂邮件</p>", true);

        // attachmentFilename 表示附件名
        // File("文件路径") 表示附件路径
        // static目录下的文件可以直接访问
        helper.addAttachment("warning.jpg", new File("E:\\Coding\\test\\temp\\NanoServe\\SpringBoot\\springboot-08-task\\target\\classes\\static\\right.jpg"));

        helper.setTo("475417309@qq.com");
        helper.setFrom("475417309@qq.com");

        mailSender.send(mimeMessage);
    }

}
