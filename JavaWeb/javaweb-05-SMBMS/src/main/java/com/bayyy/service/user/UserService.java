package com.bayyy.service.user;

import com.bayyy.entity.User;

import java.util.List;

public interface UserService {
    // 用户登录
    public User login(String userCode, String userPassword);

    // 根据用户id修改密码
    public boolean updatePwd(int id, String password);

    // 查询记录数
    public int getUserCount(String userName, int userRole);

    // 查询用户列表
    public List<User> getUserList(String userName, int userRole, int currentPageNo, int pageSize);

    //
}