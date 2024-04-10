package com.bayyy.controller;

import com.bayyy.pojo.User;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;

@Controller
@RequestMapping("/u")
public class UserController {
    // localhost:8080/u/t1?name=bayyy
    @GetMapping("/t1")
    public String test1(String name, Model model) {
        // 1. 接收前端参数
        System.out.println("接收到前端的参数为：" + name);
        // 2. 将返回的结果传递给前端
        model.addAttribute("msg", name);
        // 3. 视图跳转
        return "test";
    }

    // localhost:8080/u/t1?username=bayyy
    // @RequestParam("username") String name: 表示前端传递过来的参数username，赋值给后端的变量name
    @GetMapping("/t2")
    public String test2(@RequestParam("username") String name, Model model) {
        // 1. 接收前端参数
        System.out.println("接收到前端的参数为：" + name);
        // 2. 将返回的结果传递给前端
        model.addAttribute("msg", name);
        // 3. 视图跳转
        return "test";
    }

    // localhost:8080/u/t3?id=1&name=bayyy&age=18
    // 前端接收的是一个对象：User{id，name，age}
    @GetMapping("/t3")
    public String test3(User user, Model model) {
        // 1. 接收前端参数
        System.out.println("接收到前端的参数为：" + user);
        // 2. 将返回的结果传递给前端
        model.addAttribute("msg", user);
        // 3. 视图跳转
        return "test";
    }


}
