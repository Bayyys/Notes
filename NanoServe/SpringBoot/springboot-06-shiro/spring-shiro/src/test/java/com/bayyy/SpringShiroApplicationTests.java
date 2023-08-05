package com.bayyy;

import com.bayyy.mapper.UserMapper;
import com.bayyy.pojo.User;
import com.bayyy.service.UserServiceImpl;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

@SpringBootTest
class SpringShiroApplicationTests {
    @Autowired
    UserServiceImpl userService;

    @Test
    void contextLoads() {
//        System.out.println(userService.queryUserByName("bayyy"));
        userService.addUser(new User(5, "root", "123456"));
        userService.queryUserList().forEach(System.out::println);
    }

}
