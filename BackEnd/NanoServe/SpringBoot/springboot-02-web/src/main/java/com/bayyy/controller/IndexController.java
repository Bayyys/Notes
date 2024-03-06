package com.bayyy.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;

import java.util.Arrays;

// templates目录下的所有页面，只能通过controller来访问
// 需要模板引擎的支持(Thymeleaf)
@Controller
public class IndexController {
    @RequestMapping("/index")
    public String index() {
        return "index";
    }

    @RequestMapping("/test")
    public String test(Model model) {
        model.addAttribute("msg", "<h3>Hello, SpringBoot</h3>");
        model.addAttribute("list", Arrays.asList("张三", "李四", "王五"));
        return "test";
    }

}
