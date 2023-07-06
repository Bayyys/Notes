package com.bayyy.filter;

import javax.servlet.*;
import java.io.IOException;

// 注意: 这里的Filter是javax.servlet.Filter
public class CharacterEncodingFilter implements Filter {
    // 初始化： web 服务器启动，就已经初始化了，随时等待过滤对象出现！
    @Override
    public void init(FilterConfig filterConfig) throws ServletException {
        // 初始化
        System.out.println("CharacterEncodingFilter init");

    }

    /*filterChain: 过滤器链, 用于执行下一个过滤器
     1. 过滤器中的所有代码, 在过滤特定请求的时候都会执行
     2. 必须要让过滤器继续通行
    */
    @Override
    public void doFilter(ServletRequest servletRequest, ServletResponse servletResponse, FilterChain filterChain) throws IOException, ServletException {
        // 过滤
        System.out.println("CharacterEncodingFilter doFilter");
        servletRequest.setCharacterEncoding("utf-8");
        servletResponse.setCharacterEncoding("utf-8");
        servletResponse.setContentType("text/html;charset=utf-8");

        System.out.println("CharacterEncodingFilter 执行前...");
        // filterChain: 过滤器链, 用于执行下一个过滤器
        filterChain.doFilter(servletRequest,servletResponse);   // 让请求继续走, 如果不写, 请求将被拦截
        System.out.println("CharacterEncodingFilter 执行后...");

    }

    @Override
    public void destroy() {
        // 销毁
        System.out.println("CharacterEncodingFilter destroy");
    }
}
