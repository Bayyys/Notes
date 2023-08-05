package com.bayyy;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.scheduling.annotation.EnableAsync;
import org.springframework.scheduling.annotation.EnableScheduling;

@SpringBootApplication
@EnableScheduling  // 开启定时任务注解功能
@EnableAsync  // 开启异步注解功能
public class Springboot08TaskApplication {

    public static void main(String[] args) {
        SpringApplication.run(Springboot08TaskApplication.class, args);
    }

}
