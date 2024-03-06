package com.bayyy.filter;

import javax.servlet.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

public class SysFilter implements Filter {
    @Override
    public void init(FilterConfig filterConfig) throws ServletException {
        System.out.println("SysFilter init");
    }

    @Override
    public void doFilter(ServletRequest servletRequest, ServletResponse servletResponse, FilterChain filterChain) throws IOException, ServletException {
        System.out.println("SysFilter doFilter");

        HttpServletRequest request = (HttpServletRequest) servletRequest;
        HttpServletResponse response = (HttpServletResponse) servletResponse;

        Object user_session = request.getSession().getAttribute("USER_SESSION");

        if (user_session == null) {
            response.sendRedirect(request.getContextPath()+"/error/notfind.jsp");
        }
        filterChain.doFilter(servletRequest,servletResponse);

    }

    @Override
    public void destroy() {
        System.out.println("SysFilter destroy");
    }
}
