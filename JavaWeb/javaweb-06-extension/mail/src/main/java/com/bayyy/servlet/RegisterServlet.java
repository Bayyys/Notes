package com.bayyy.servlet;

import com.bayyy.pojo.User;
import com.bayyy.utils.SendMail;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

public class RegisterServlet extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        // 接收用户请求
        String username = req.getParameter("username");
        String password = req.getParameter("password");
        String email = req.getParameter("email");

        User user = new User(username, password, email);

        // 用户注册成功后，会给用户发送一封邮件
        // 使用多线程给用户发送邮件， 防止出现耗时操作, 用户体验不好
        SendMail sendMail = new SendMail(user);
        // 启动线程, 启动后会自动执行run方法
        sendMail.start();

        // 注册用户
        req.setAttribute("msg", "注册成功, 已通过电子邮箱向您发送注册信息, 请注意查收! ");
        req.getRequestDispatcher("info.jsp").forward(req, resp);
    }

    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        doGet(req,resp);
    }
}
