package com.bayyy.dao.user;

import com.bayyy.entity.User;

import java.sql.Connection;
import java.sql.SQLException;
import java.util.List;

public interface UserDao {
    // 得到登录的用户
    public User getLoginUser(Connection connection, String serCode) throws SQLException;

    // 修改当前用户密码
    public int updatePwd(Connection connection, int id, String password) throws SQLException;

    // 查询用户名或者角色查询用户总数
    public int getUserCount(Connection connection, String userName, int userRole) throws SQLException;

    // 获取用户列表(通过条件查询-userList)
    public List<User> getUserList(Connection connection, String userName, int userRole, int currentPageNo, int pageSize) throws SQLException;

}
