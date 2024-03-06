package com.bayyy.service;

import com.bayyy.pojo.User;

import java.util.List;

public interface UserService {
    public List<User> queryUserList();
    public User queryUserByName(String name);
    public int addUser(User user);

}
