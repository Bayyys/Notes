package com.bayyy.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
@RequestMapping("/c3")  // 以下所有的方法都在/c3下
public class ControllerTest3 {
    @RequestMapping("/t1")  // 访问路径为/c3/t1
    public String test1(Model model) {
        model.addAttribute("msg","ControllerTest3");
        return "test";
    }
}
