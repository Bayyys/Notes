package com.bayyy;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;
import java.io.IOException;

public class SessionDemo01 extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        System.out.println("进入了SessionDemo01方法");
        // 解中文决乱码问题
        req.setCharacterEncoding("utf-16");
        resp.setCharacterEncoding("utf-16");

        // Session，服务器从客户端获取
        HttpSession session = req.getSession();

        // 存储
        session.setAttribute("name", "bayyy");
        session.setAttribute("pwd", "123456");

        // 获取ID
        String sessionId = session.getId();

        // 判断Session是否是新创建的
        if (session.isNew()) {
            resp.getWriter().write("Session创建成功，ID为：" + sessionId);
        } else {
            resp.getWriter().write("Session已经在服务器中存在了，ID为：" + sessionId);
        }
    }

    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        doGet(req, resp);
    }
}
