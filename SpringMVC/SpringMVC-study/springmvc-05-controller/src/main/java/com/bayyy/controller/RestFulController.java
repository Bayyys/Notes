package com.bayyy.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

@Controller
public class RestFulController {
    // 原来的：http://localhost:8080/add?a=1&b=2
    // RestFul：http://localhost:8080/add/1/2
    // @PathVariable 路径变量: 获得路径中的值
    @RequestMapping(value = "/add/{a}/{b}", method = RequestMethod.GET)
    public String test1(@PathVariable int a, @PathVariable String b, Model model) {
        String res = a + b;
        model.addAttribute("msg","a=" + a + " b=" + b +" 结果为" + res);
        return "test";
    }
}
