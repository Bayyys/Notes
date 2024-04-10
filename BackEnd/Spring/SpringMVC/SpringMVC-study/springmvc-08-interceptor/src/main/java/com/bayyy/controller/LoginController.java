package com.bayyy.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;

import javax.servlet.http.HttpSession;

@Controller
@RequestMapping("/user")
public class LoginController {
    @RequestMapping("/login")
    public String login(@RequestParam("username") String name, @RequestParam("password") String pwd, HttpSession session) {
        // 模拟登录, 将用户信息保存到session中
        session.setAttribute("user", name);
        System.out.println(session.getAttribute("user"));
        return "main";
    }

    @RequestMapping("/goLogin")
    public String goLogin(HttpSession session) {
        return "login";
    }

    @RequestMapping("/logout")
    public String logout(HttpSession session) {
        session.removeAttribute("user");
        return "login";
    }

    @RequestMapping("/main")
    public String main() {
        return "main";
    }
}
