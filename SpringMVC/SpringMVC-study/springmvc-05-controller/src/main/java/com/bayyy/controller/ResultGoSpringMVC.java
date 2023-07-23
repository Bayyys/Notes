package com.bayyy.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
public class ResultGoSpringMVC {
    @RequestMapping("/r2/t1")
    public String test1(Model model) throws Exception {
        model.addAttribute("msg", "/WEB-INF/jsp/test.jsp");
        // 转发到视图
        return "/WEB-INF/jsp/test.jsp";
    }

    @RequestMapping("/r2/t2")
    public String test3(Model model) throws Exception {
        model.addAttribute("msg", "forward:/test.jsp");
        // 转发到视图
        return "forward:/WEB-INF/jsp/test.jsp";
    }

    @RequestMapping("/r2/t3")
    public String test2(Model model) throws Exception {
//        model.addAttribute("msg", "redirect:/test.jsp");
        // 重定向到视图
        return "redirect:/WEB-INF/jsp/test.jsp";
    }
}
