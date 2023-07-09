package com.bayyy.dao.user;

import com.bayyy.entity.User;

import java.sql.Connection;
import java.sql.SQLException;

public interface UserDao {
    // 得到登录的用户
    public User getLoginUser(Connection connection, String serCode) throws SQLException;
}
