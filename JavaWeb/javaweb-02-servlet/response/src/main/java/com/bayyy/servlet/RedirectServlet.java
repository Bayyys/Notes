package com.bayyy.servlet;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

public class RedirectServlet extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        System.out.println("进入了RedirectServlet");
//        resp.sendRedirect("/servlet/verify");   // 重定向: /verify(x) 相对于根目录, 则需要加上 /servlet/verify
//        resp.sendRedirect("verify");    // 重定向: verify 则是相对路径，相对于当前路径，即 /servlet/verify
        resp.setHeader("Location", "verify"); // 重定向
        resp.setStatus(HttpServletResponse.SC_FOUND);    // 302
    }

    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        doGet(req, resp);
    }
}
