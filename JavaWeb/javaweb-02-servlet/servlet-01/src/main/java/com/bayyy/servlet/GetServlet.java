package com.bayyy.servlet;

import javax.servlet.ServletContext;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

public class GetServlet extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        ServletContext context = this.getServletContext();
        String username = (String) context.getAttribute("username");

        resp.setHeader("content-type", "text/html;charset=utf-8");  // 中文乱码问题解决: resp.setHeader("content-type", "text/html;charset=utf-8");
//         或者
//        resp.setContentType("text/html");
//        resp.setCharacterEncoding("utf-8");
//        resp.getWriter().print("name: " + username);
        resp.getWriter().print("名字: " + username);  // 中文乱码问题解决: resp.setHeader("content-type", "text/html;charset=utf-8");
    }

    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        doGet(req, resp);
    }
}
