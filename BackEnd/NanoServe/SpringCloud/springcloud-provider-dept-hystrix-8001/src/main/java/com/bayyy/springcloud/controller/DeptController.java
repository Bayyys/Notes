package com.bayyy.springcloud.controller;

import com.bayyy.springcloud.pojo.Dept;
import com.bayyy.springcloud.service.DeptService;
import com.netflix.hystrix.contrib.javanica.annotation.DefaultProperties;
import com.netflix.hystrix.contrib.javanica.annotation.HystrixCommand;
import lombok.Builder;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.cloud.netflix.hystrix.EnableHystrix;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;

// 提供Restful服务
@RestController
public class DeptController {
    @Autowired
    DeptService service;

    @GetMapping("/dept/get/{id}")
    @HystrixCommand(fallbackMethod = "hystrixGetDeptById")
    // 一旦调用服务方法失败并抛出了错误信息后，会自动调用@HystrixCommand标注好的fallbackMethod调用类中的指定方法
    public Dept queryById(@PathVariable("id") Long deptId) {
        Dept dept = service.queryById(deptId);
        if (dept == null) {
            throw new RuntimeException("这个id=>" + deptId + ",不存在该用户，或信息无法找到~");
        }
        return dept;
    }

    //根据id查询备选方案(熔断)
    public Dept hystrixGetDeptById(@PathVariable("id") Long deptId) {
        System.out.println("熔断方法");
        return new Dept().setDeptId(deptId)
                .setDname("这个id=>" + deptId + ",没有对应的信息,null---@Hystrix~")
                .setDbSource("在MySQL中没有这个数据库");
    }
}
