package com.bayyy.springcloud.service;

import com.bayyy.springcloud.pojo.Dept;

import java.util.List;

public interface DeptService {
    public boolean addDept(Dept dept);
    public Dept queryById(Long deptId);
    public List<Dept> queryAll();
}
