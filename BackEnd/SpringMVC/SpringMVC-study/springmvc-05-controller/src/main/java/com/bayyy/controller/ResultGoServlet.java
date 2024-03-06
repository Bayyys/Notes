package com.bayyy.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

@Controller
public class ResultGoServlet {
    @RequestMapping("/r1/t1")
    public String test1(HttpServletRequest request, HttpServletResponse response) throws Exception {
        HttpSession session = request.getSession();
        System.out.println(session.getId());
        return "test";
    }

    @RequestMapping("/r1/t2")
    public String test2(HttpServletRequest request, HttpServletResponse response) throws Exception {
        HttpSession session = request.getSession();
        System.out.println(session.getId());
        return "test";
    }

    @RequestMapping("/r1/t3")
    public String test3(HttpServletRequest request, HttpServletResponse response) throws Exception {
        HttpSession session = request.getSession();
        System.out.println(session.getId());
        return "test";
    }
}
