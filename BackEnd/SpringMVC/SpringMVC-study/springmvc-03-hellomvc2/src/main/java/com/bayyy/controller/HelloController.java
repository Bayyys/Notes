package com.bayyy.controller;

import org.springframework.web.servlet.ModelAndView;
import org.springframework.web.servlet.mvc.Controller;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class HelloController implements Controller {
    @Override
    public ModelAndView handleRequest(HttpServletRequest request, HttpServletResponse response) throws Exception {
        ModelAndView mv = new ModelAndView();
        // 业务代码
        String result = "HelloSpringMVC";
        mv.addObject("msg", result);

        // 视图跳转
        mv.setViewName("test"); // /WEB-INF/jsp/test.jsp

        return mv;
    }
}
