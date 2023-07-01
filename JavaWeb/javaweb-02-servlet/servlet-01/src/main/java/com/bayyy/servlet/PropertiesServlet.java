package com.bayyy.servlet;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.io.InputStream;
import java.util.Properties;

public class PropertiesServlet extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        System.out.println("进入了PropertiesServlet");
        InputStream resourceAsStream = this.getServletContext().getResourceAsStream("/WEB-INF/classes/db.properties");// 读取资源文件
        Properties prop = new Properties(); // 创建一个Properties对象
        prop.load(resourceAsStream); // 加载资源文件
        String username = prop.getProperty("username"); // 通过key获取value
        String pwd = prop.getProperty("pwd");

        resp.getWriter().print("username: " + username + ",  pwd: " + pwd);

    }

    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        doGet(req, resp);
    }
}
