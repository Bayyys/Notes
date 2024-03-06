package com.bayyy.servlet.user;

import com.bayyy.entity.User;
import com.bayyy.service.user.UserService;
import com.bayyy.service.user.UserServiceImpl;
import com.bayyy.utils.Constants;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

public class LoginServlet extends HttpServlet {
    // Servlet: 控制层, 调用业务层代码
    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        System.out.println("LoginServlet--start...");
        // 获取用户名和密码
        String userCode = req.getParameter("userCode");
        String userPassword = req.getParameter("userPassword");
        
        // 和数据库中的密码进行对比, 调用业务层
        UserService userService = new UserServiceImpl();
        User user = userService.login(userCode, userPassword);
        if (user != null) { // 查有此人, 可以登录
            // 将用户的信息放到Session中
            req.getSession().setAttribute(Constants.USER_SESSION, user);
            // 跳转到主页
            resp.sendRedirect("jsp/frame.jsp"); // 重定向
        } else {
            // 转发回登录页面, 并提示错误信息
            req.setAttribute("error", "用户名或密码不正确");
            req.getRequestDispatcher("login.jsp").forward(req, resp);   // 转发
        }

    }

    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        doGet(req, resp);
    }
}
