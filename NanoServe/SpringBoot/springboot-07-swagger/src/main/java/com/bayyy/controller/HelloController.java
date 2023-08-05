package com.bayyy.controller;

import com.bayyy.pojo.User;
import io.swagger.annotations.ApiOperation;
import io.swagger.annotations.ApiParam;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HelloController {
    @RequestMapping("/hello") // http://localhost:8080/hello
    public String hello() {
        return "Hello Spring Boot!";
    }

    @RequestMapping("/bayyy/hello")
    public String bayyyHello() {
        return "Hello Bayyy!";
    }

    @RequestMapping("/user")
    public User user() {
        return new User();
    }

    @GetMapping("/test")
    @ApiOperation("测试接口")
    public String test(@ApiParam("测试输入数据") String text) {
        text = text + "test";
        return text;
    }
}
