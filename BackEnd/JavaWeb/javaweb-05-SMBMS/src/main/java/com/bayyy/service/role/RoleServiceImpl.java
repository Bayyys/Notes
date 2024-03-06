package com.bayyy.service.role;

import com.bayyy.dao.BaseDao;
import com.bayyy.dao.role.RoleDao;
import com.bayyy.dao.role.RoleDaoImpl;
import com.bayyy.entity.Role;
import org.junit.Test;

import java.sql.Connection;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

public class RoleServiceImpl implements RoleService {
    // 引入Dao
    private RoleDao roleDao;
    public RoleServiceImpl() {
        roleDao = new RoleDaoImpl();
    }
    @Override
    public List<Role> getRoleList(){
        Connection connection = null;
        List<Role> roleList = null;
        try {
            connection = BaseDao.getConnection();
            roleList = roleDao.getRoleList(connection);
        } catch (SQLException e) {
            throw new RuntimeException(e);
        } finally {
            BaseDao.closeResource(connection, null, null);
        }
        return roleList;
    }

    @Test
    public void test() {
        RoleServiceImpl roleService = new RoleServiceImpl();
        List<Role> roleList = roleService.getRoleList();
        for (Role role : roleList) {
            System.out.println(role.getRoleName());
        }
    }
}
