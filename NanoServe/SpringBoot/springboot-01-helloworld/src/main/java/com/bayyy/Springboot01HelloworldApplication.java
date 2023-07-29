package com.bayyy;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication      // 标注这个类是一个SpringBoot的应用
public class Springboot01HelloworldApplication {

    public static void main(String[] args) {
        // 将SpringBoot应用启动
        SpringApplication.run(Springboot01HelloworldApplication.class, args);
    }

}
