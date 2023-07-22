package com.bayyy.mapper;

import com.bayyy.pojo.User;

import java.util.List;

public interface UserMapper {
    List<User> selectUser();
    User selectUserById(int id);
    int addUser(User user);
    int deleteUser(int id);
}
