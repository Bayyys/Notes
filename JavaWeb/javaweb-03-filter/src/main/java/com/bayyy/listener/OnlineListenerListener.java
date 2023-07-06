package com.bayyy.listener;

import javax.servlet.ServletContext;
import javax.servlet.http.HttpSessionEvent;
import javax.servlet.http.HttpSessionListener;

// 统计网站在线人数: 统计session
public class OnlineListenerListener implements HttpSessionListener {
    // 创建session监听
    // 一旦创建session就会触发一次这个事件
    @Override
    public void sessionCreated(HttpSessionEvent se) {
        ServletContext ctx = se.getSession().getServletContext();
        System.out.println(se.getSession().getId());
        Integer onlineCount = (Integer) ctx.getAttribute("OnlineCount");

        if (onlineCount == null) {  // 判断session是否是第一次创建
            onlineCount = 1;   // 首次访问
        } else {
            int count = onlineCount; // 获取在线人数
            onlineCount = count + 1;   // 在线人数加一
        }
        ctx.setAttribute("OnlineCount", onlineCount);
    }

    // 销毁session监听
    // 一旦销毁session就会触发一次这个事件
    @Override
    public void sessionDestroyed(HttpSessionEvent se) {
        ServletContext ctx = se.getSession().getServletContext();
        Integer onlineCount = (Integer) ctx.getAttribute("OnlineCount");

        if (ctx.getAttribute("OnlineCount") == null) {
            onlineCount = 0;
        } else {
            int count = onlineCount;
            onlineCount = count - 1;
        }
        ctx.setAttribute("OnlineCount", onlineCount);
    }
}
