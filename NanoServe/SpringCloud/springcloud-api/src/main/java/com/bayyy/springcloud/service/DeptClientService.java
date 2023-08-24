package com.bayyy.springcloud.service;

import com.bayyy.springcloud.pojo.Dept;
import org.springframework.cloud.openfeign.FeignClient;
import org.springframework.stereotype.Component;
import org.springframework.stereotype.Service;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;

import java.util.List;

@Service
@FeignClient(value = "SPRINGCLOUD-PROVIDER-DEPT")
public interface DeptClientService {
    @GetMapping("/dept/add")
    public boolean addDept(Dept dept);

    @GetMapping("/dept/get/{id}")
    public Dept queryById(@PathVariable("id") Long deptId);

    @GetMapping("/dept/list")
    public List<Dept> queryAll();
}
