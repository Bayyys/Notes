package com.bayyy.servlet;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

public class RequestTest extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        System.out.println("进入了RequestTest");
        String username = req.getParameter( "username");
        String password = req.getParameter( "password");

        System.out.println(username+":"+password);

        resp.sendRedirect("success.jsp");   // 可以直接写重定向的位置 !不可以加‘/’!
//        resp.sendRedirect("/servlet/success.jsp");
    }

    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        doGet(req, resp);
    }
}
