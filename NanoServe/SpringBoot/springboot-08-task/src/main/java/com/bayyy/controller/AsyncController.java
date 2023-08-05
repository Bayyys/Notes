package com.bayyy.controller;

import com.bayyy.service.AsyncService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ResponseBody;

@Controller
public class AsyncController {
    @Autowired
    AsyncService asyncService;

    @GetMapping("/async")
    @ResponseBody
    public String async(){
        // 输出总用时
        long start = System.currentTimeMillis();
        asyncService.hello();
        long end = System.currentTimeMillis();
        String time = "总用时：" + (end - start) + "ms";
        return time;
    }
}
