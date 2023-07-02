package com.bayyy;

import javax.servlet.ServletException;
import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.xml.crypto.Data;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.Date;

public class CookieDemo01 extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        System.out.println("进入了CookieDemo01方法");
        // 解中文决乱码问题
        req.setCharacterEncoding("utf-16");
        resp.setCharacterEncoding("utf-16");

        PrintWriter out = resp.getWriter();

        // Cookie，服务器从客户端获取
        Cookie[] cookies = req.getCookies();    // 这里返回数组，说明Cookie可能存在多个

        // 判断Cookie是否存在
        if (cookies != null) {
            // 如果存在
            out.write(String.valueOf("你上一次访问的时间是："));
            for (int i = 0; i < cookies.length; i++) {
                Cookie cookie = cookies[i];
                // 获取Cookie的名字
                if (cookie.getName().equals("LastLoginTime")) {
                    // 获取Cookie的值
                    long lastLoginTime = Long.parseLong(cookie.getValue());
                    Date date = new Date(lastLoginTime);
                    out.write(date.toLocaleString());
                }
            }
        } else {
            // 如果不存在
            out.write("这是您第一次访问本站！");
        }
        Cookie cookie = new Cookie("LastLoginTime", System.currentTimeMillis() + "");
        resp.addCookie(cookie);
    }

    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws
            ServletException, IOException {
        doGet(req, resp);
    }
}
