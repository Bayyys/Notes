package com.bayyy.springcloud.dao;

import com.bayyy.springcloud.pojo.Dept;
import org.apache.ibatis.annotations.Mapper;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
@Mapper
public interface DeptDao {
    public boolean addDept(Dept dept);

    public Dept queryById(Long deptId);

    public List<Dept> queryAll();
}
