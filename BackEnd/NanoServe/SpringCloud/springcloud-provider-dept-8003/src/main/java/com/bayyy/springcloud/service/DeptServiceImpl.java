package com.bayyy.springcloud.service;

import com.bayyy.springcloud.dao.DeptDao;
import com.bayyy.springcloud.pojo.Dept;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class DeptServiceImpl implements DeptService {
    // Service层调用Dao层
    @Autowired
    private DeptDao deptDao;

    @Override
    public boolean addDept(Dept dept) {
        return deptDao.addDept(dept);
    }

    @Override
    public Dept queryById(Long deptId) {
        return deptDao.queryById(deptId);
    }

    @Override
    public List<Dept> queryAll() {
        return deptDao.queryAll();
    }
}


