package com.bayyy.servlet;

import javax.servlet.ServletContext;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

public class HelloServlet extends HttpServlet {
    // 由于get或者post只是请求实现的不同的方式，可以相互调用，业务逻辑都一样；
    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        System.out.println("doGet 方法被调用");

        // this.getInitParameter()   初始化参数(现在基本不用了)
        // this.getServletConfig()   Servlet配置
        // this.getServletContext()  Servlet上下文
        ServletContext context = this.getServletContext();

        String username = "bayyy"; //数据
        context.setAttribute("username", username); //将一个数据保存在了ServletContext中，名字为：username:
    }

    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        doGet(req, resp);
    }
}
