package com.bayyy.service.user;

import com.bayyy.entity.User;

public interface UserService {
    // 用户登录
    public User login(String userCode, String userPassword);

    // 根据用户id修改密码
    public boolean updatePwd(int id, String password);
}