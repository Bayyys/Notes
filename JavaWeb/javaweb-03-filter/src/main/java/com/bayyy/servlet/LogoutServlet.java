package com.bayyy.servlet;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

public class LogoutServlet extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        System.out.println("LogoutServlet doGet");
//        req.getSession().invalidate(); // 实际操作中不建议删除session，而是将session设置为失效
        Object user_session = req.getSession().getAttribute("USER_SESSION");
        if (user_session != null) {
            req.getSession().removeAttribute("USER_SESSION");
            resp.sendRedirect(req.getContextPath()+"/login.jsp");
        } else {
            resp.sendRedirect(req.getContextPath()+"/login.jsp");
        }
    }

    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        doGet(req,resp);
    }
}
