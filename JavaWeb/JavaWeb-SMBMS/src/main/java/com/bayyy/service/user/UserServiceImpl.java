package com.bayyy.service.user;

import com.bayyy.dao.BaseDao;
import com.bayyy.dao.user.UserDao;
import com.bayyy.dao.user.UserDaoImpl;
import com.bayyy.entity.User;
import org.junit.jupiter.api.Test;

import java.sql.Connection;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

public class UserServiceImpl implements UserService{
    // 业务层都会调用dao层, 通过用户编码获取用户信息
    private UserDao userDao;
    public UserServiceImpl() {
        userDao = new UserDaoImpl();
    }

    @Override
    public User login(String userCode, String userPassword) {
        Connection connection = null;
        User user = null;

        try {
            connection = BaseDao.getConnection();
            user = userDao.getLoginUser(connection, userCode);
        } catch (SQLException e) {
            throw new RuntimeException(e);
        } finally {
            BaseDao.closeResource(connection, null, null);
        }
        return user;
    }

    @Override
    public boolean updatePwd(int id, String password) {
        Connection connection = null;
        boolean flag = false;

        // 修改密码
        try {
            connection = BaseDao.getConnection();
            if (userDao.updatePwd(connection, id, password) > 0) {
                System.out.println("修改密码成功" + password);
                flag = true;
            }
        } catch (SQLException e) {
            throw new RuntimeException(e);
        } finally {
            BaseDao.closeResource(connection, null, null);
        }
        return flag;
    }

    @Override
    public int getUserCount(String userName, int userRole) {
        Connection connection = null;
        int count = 0;

        try {
            connection = BaseDao.getConnection();
            count = userDao.getUserCount(connection, userName, userRole);
        } catch (SQLException e) {
            throw new RuntimeException(e);
        } finally {
            BaseDao.closeResource(connection, null, null);
        }
        return count;
    }

    @Override
    public List<User> getUserList(String userName, int userRole, int currentPageNo, int pageSize) {
        Connection connection = null;
        List<User> userList = null;
        try {
            connection = BaseDao.getConnection();
            userList = userDao.getUserList(connection, userName, userRole, currentPageNo, pageSize);
        } catch (SQLException e) {
            throw new RuntimeException(e);
        } finally {
            BaseDao.closeResource(connection, null, null);
        }
        return userList;
    }

    @Test
    public void test() {
        // 测试UserServiceImpl
        UserServiceImpl userService = new UserServiceImpl();
        List<User> userList = userService.getUserList("", 0, 1, 12);
        for (User user : userList) {
            System.out.println(user.getUserName());
        }
    }
}
