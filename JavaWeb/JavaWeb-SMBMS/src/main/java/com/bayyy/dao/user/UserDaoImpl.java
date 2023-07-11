package com.bayyy.dao.user;

import com.bayyy.dao.BaseDao;
import com.bayyy.entity.User;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class UserDaoImpl implements UserDao {
    @Override
    public User getLoginUser(Connection connection, String serCode) throws SQLException {
        PreparedStatement preparedStatement = null;
        ResultSet resultSet = null;
        User user = null;

        if (connection != null) {
            String sql = "select * from smbms_user where userCode=?";
            Object[] params = {serCode};
            resultSet = BaseDao.execute(connection, sql, params, resultSet, preparedStatement);
            if (resultSet.next()) {
                user = new User();
                user.setId(resultSet.getInt("id"));                           // id
                user.setUserCode(resultSet.getString("userCode"));    // 用户编码
                user.setUserName(resultSet.getString("userName"));    // 用户名称
                user.setUserPassword(resultSet.getString("userPassword"));    // 用户密码
                user.setGender(resultSet.getInt("gender"));                   // 性别
                user.setBirthday(resultSet.getDate("birthday"));              // 出生日期
                user.setPhone(resultSet.getString("phone"));                  // 电话
                user.setAddress(resultSet.getString("address"));              // 地址
                user.setUserRole(resultSet.getInt("userRole"));    // 用户角色
                user.setCreatedBy(resultSet.getInt("createdBy")); // 创建者
                user.setCreationDate(resultSet.getTimestamp("creationDate")); // 创建时间
                user.setModifyBy(resultSet.getInt("modifyBy"));     // 更新者
                user.setModifyDate(resultSet.getTimestamp("modifyDate"));     // 更新时间
            }
            BaseDao.closeResource(null, preparedStatement, resultSet);
        }
        return user;
    }

    @Override
    public int updatePwd(Connection connection, int id, String password) throws SQLException {
        PreparedStatement preparedStatement = null;
        int execute = 0;

        if (connection != null) {
            Object prams[] = {password, id};
            String sql = "update smbms_user set userPassword=? where id=?";
            execute = BaseDao.execute(connection, sql, prams, preparedStatement);
            BaseDao.closeResource(null, preparedStatement, null);
            return 0;
        }
        return execute;
    }
}
