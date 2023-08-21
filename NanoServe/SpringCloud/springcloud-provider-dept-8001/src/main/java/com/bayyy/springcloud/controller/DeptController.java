package com.bayyy.springcloud.controller;

import com.bayyy.springcloud.pojo.Dept;
import com.bayyy.springcloud.service.DeptService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.cloud.client.discovery.EnableDiscoveryClient;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RestController;

// 提供Restful服务
@RestController
public class DeptController {
    @Autowired
    DeptService deptService;

    @PostMapping("/dept/add")
    public boolean addDept(Dept dept) {
        return deptService.addDept(dept);
    }

    @GetMapping("/dept/get/{id}")
    public Dept queryById(@PathVariable("id") Long deptId) {
        return deptService.queryById(deptId);
    }

    @GetMapping("/dept/list")
    public Object queryAll() {
        return deptService.queryAll();
    }
}
