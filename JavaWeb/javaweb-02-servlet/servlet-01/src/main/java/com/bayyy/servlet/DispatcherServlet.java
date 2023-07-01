package com.bayyy.servlet;

import javax.servlet.ServletContext;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

public class DispatcherServlet extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        ServletContext context = this.getServletContext();

        System.out.println("进入了dispatcherServlet");
//        RequestDispatcher requestDispatcher = context.getRequestDispatcher("/getHello");    // 请求转发的请求路径
//        requestDispatcher.forward(req, resp);  // 调用forward实现请求转发
        context.getRequestDispatcher("/getHello").forward(req, resp);  // 调用forward实现请求转发
    }

    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        doGet(req, resp);
    }
}
