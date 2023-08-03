package com.bayyy.controller;

import com.bayyy.mapper.UserMapper;
import com.bayyy.pojo.User;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
public class UserController {
    @Autowired
    private UserMapper userMapper;

    @GetMapping("/list")
    public List<User> userList() {
        List<User> users = userMapper.selectUser();
        return users;
    }

    @GetMapping("/list/{id}")
    public User userById(@PathVariable("id") int id) {
        System.out.println("id = " + id);
        return userMapper.selectUserById(id);
    }

    @GetMapping("/add")
    public String addUser() {
        System.out.println("add");
        User user = new User();
        user.setId(6);
        user.setUsername("Bayyy");
        int res = userMapper.addUser(user);
        if (res > 0) {
            return "add success";
        } else {
            return "add failed";
        }
    }

    @GetMapping("/update/{id}")
    public String update(@PathVariable("id") int id){
        User user = new User();
        user.setId(id);
        user.setUsername("New_Bayyy");
        int res = userMapper.updateUser(user);
        if (res > 0) {
            return "update success";
        } else {
            return "update failed";
        }
    }

    @GetMapping("/delete/{id}")
    public String delete(@PathVariable("id") int id){
        int res = userMapper.deleteUser(id);
        if (res > 0) {
            return "delete success";
        } else {
            return "delete failed";
        }
    }


}
