package com.bayyy.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HelloController {
    @RequestMapping("/hello") // http://localhost:8080/hello
    public String hello() {
        return "Hello Spring Boot!";
    }
}
