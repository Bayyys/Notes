package com.bayyy.filter;

import com.bayyy.entity.User;
import com.bayyy.utils.Constants;

import javax.servlet.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

public class SysFilter implements Filter {
    @Override
    public void init(FilterConfig filterConfig) throws ServletException {
    }

    @Override
    public void doFilter(ServletRequest servletRequest, ServletResponse servletResponse, FilterChain filterChain) throws IOException, ServletException {
        HttpServletRequest request = (HttpServletRequest) servletRequest;
        HttpServletResponse respone = (HttpServletResponse) servletResponse;

        // 过滤器, 从Session中获取用户
        User user = (User) request.getSession().getAttribute(Constants.USER_SESSION);

        if (user == null) { // Session失效, 用户不存在(注销或者未登录)
            // 已经被移除或者注销了, 或者未登录
            respone.sendRedirect("/error.jsp"); // 跳转到错误页面
        } else {
            filterChain.doFilter(servletRequest, servletResponse);  // 放行
        }
    }

    @Override
    public void destroy() {
    }
}
