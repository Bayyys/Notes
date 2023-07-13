package com.bayyy.dao.user;

import com.bayyy.dao.BaseDao;
import com.bayyy.entity.Role;
import com.bayyy.entity.User;
import com.mysql.cj.util.StringUtils;

import java.sql.*;
import java.util.ArrayList;
import java.util.List;

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
            return execute;
        }
        return execute;
    }

    // 查询用户名或者角色查询用户总数
    @Override
    public int getUserCount(Connection connection, String userName, int userRole) throws SQLException {
        PreparedStatement preparedStatement = null;
        ResultSet resultSet = null;
        int count = 0;

        if (connection != null) {
            StringBuffer sql = new StringBuffer();
            sql.append("select count(1) as count from smbms_user u,smbms_role r where u.userRole=r.id");
            // 存放参数
            ArrayList<Object> list = new ArrayList<Object>();
            if (!StringUtils.isNullOrEmpty(userName)) {
                sql.append(" and u.userName like ?");
                list.add("%" + userName + "%");
            }
            if (userRole != 0) {
                sql.append(" and u.userRole=?");
                list.add(userRole);
            }
            Object[] objects = list.toArray();
            resultSet = BaseDao.execute(connection, sql.toString(), objects, resultSet, preparedStatement);
            if (resultSet.next()) {
                count = resultSet.getInt("count");
            }
            BaseDao.closeResource(null, preparedStatement, resultSet);
        }
        return count;
    }

    @Override
    public List<User> getUserList(Connection connection, String userName, int userRole, int currentPageNo, int pageSize) throws SQLException {
        PreparedStatement preparedStatement = null;
        ResultSet resultSet = null;
        List<User> userList = new ArrayList<User>();
        if (connection != null) {
            StringBuffer sql = new StringBuffer();
            sql.append("select u.*,r.roleName as userRoleName from smbms_user u,smbms_role r where u.userRole=r.id");
            ArrayList<Object> list = new ArrayList<Object>();
            if (!StringUtils.isNullOrEmpty(userName)) {
                sql.append(" and u.userName like ?");
                list.add("%" + userName + "%");
            }
            if (userRole != 0) {
                sql.append(" and u.userRole=?");
                list.add(userRole);
            }
            // 在数据库中，分页使用limit startIndex,pageSize; 总数
            sql.append(" order by creationDate DESC limit ?,?");
            currentPageNo = (currentPageNo - 1) * pageSize;
            list.add(currentPageNo);
            list.add(pageSize);

            Object[] params = list.toArray();
            resultSet = BaseDao.execute(connection, sql.toString(), params, resultSet, preparedStatement);

            while (resultSet.next()) {
                User _user = new User();
                _user.setId(resultSet.getInt("id"));                           // id
                _user.setUserCode(resultSet.getString("userCode"));    // 用户编码
                _user.setUserName(resultSet.getString("userName"));    // 用户名称
                _user.setGender(resultSet.getInt("gender"));
                _user.setBirthday(resultSet.getDate("birthday"));
                _user.setPhone(resultSet.getString("phone"));
                _user.setUserRole(resultSet.getInt("userRole"));
                _user.setUserRoleName(resultSet.getString("userRoleName"));
                userList.add(_user);
            }
            BaseDao.closeResource(null, preparedStatement, resultSet);
        }
        return userList;
    }


}
