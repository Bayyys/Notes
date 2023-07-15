package com.bayyy.service.role;

import com.bayyy.entity.Role;

import java.sql.SQLException;
import java.util.List;

public interface RoleService {
    // 获取角色列表
    public List<Role> getRoleList();
}
