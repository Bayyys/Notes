package com.bayyy.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;

@Controller
public class CharacterEncodingTest {
    @RequestMapping("/form/t1")
    public String test1(@RequestParam("name") String name, Model model) {
        model.addAttribute("msg", name);
        System.out.println(name);
        return "test";
    }
}
