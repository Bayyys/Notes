package com.bayyy.servlet;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

public class LoginServlet extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        System.out.println("LoginServlet doGet");
        String username = req.getParameter("username");
        String password = req.getParameter("password");
        if ( username != null && username.equals("root")) {
            if (password.equals("root")) {
                req.getSession().setAttribute("USER_SESSION", req.getSession().getId());
                resp.getWriter().write("管理员登录成功");
                resp.sendRedirect(req.getContextPath()+"/sys/success.jsp");
            } else {
                resp.getWriter().write("用户名或密码错误");
                resp.sendRedirect(req.getContextPath()+"/error/pwd.jsp");
            }
        } else if (username == null || username.equals("123456")) {
            resp.getWriter().write("用户名错误");
            resp.sendRedirect(req.getContextPath()+"/error/username.jsp");
        } else {
            if (password.equals("123456")) {
                resp.getWriter().write("用户登录成功");
                resp.sendRedirect(req.getContextPath()+"/sys/success.jsp");
            } else {
                resp.getWriter().write("Login Failed");
                resp.sendRedirect(req.getContextPath()+"/error/pwd.jsp");
            }
        }
    }

    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        doGet(req,resp);
    }
}
