package com.bayyy.controller;

import org.apache.ibatis.annotations.ResultMap;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;

import javax.xml.ws.RequestWrapper;

@Controller // 代表这个类会被Spring接管，被这个注解的类中的所有方法，如果返回值是String，并且有具体页面可以跳转，那么就会被视图解析器解析
@RequestMapping("/hello")   // 代表所有的方法请求地址都是在/hello下，比如/hello/h1
public class HelloController {
    @RequestMapping("/h1")  // 请求地址: 会在/hello下拼接/h1
    public String hello(Model model){
        // 封装数据
        model.addAttribute("msg", "HelloSpringMVCAnnotation");
        System.out.println("hello");
        // return的是视图名
        return "hello"; // 会被视图解析器处理，跳转到/WEB-INF/jsp/hello.jsp
    }
}
