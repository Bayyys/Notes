package com.bayyy.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

// templates目录下的所有页面，只能通过controller来访问
// 需要模板引擎的支持(Thymeleaf)
@Controller
public class IndexController {
    @RequestMapping("/index")
    public String index() {
        return "index";
    }
}
