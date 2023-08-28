package com.bayyy.springcloud.controller;

import com.bayyy.springcloud.pojo.Dept;
import com.bayyy.springcloud.service.DeptClientService;
import com.netflix.hystrix.contrib.javanica.annotation.HystrixCommand;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.client.RestTemplate;

import java.util.List;

@RestController
public class DeptConsumerController {
    @Autowired
    private DeptClientService service;

    @RequestMapping("/consumer/dept/add")
    public boolean add(Dept dept) {
        return service.add(dept);
    }

    @RequestMapping("/consumer/dept/get/{id}")
//    @HystrixCommand(fallbackMethod = "hystrixGet") // 一旦调用服务方法失败并抛出了错误信息后，会自动调用 @HystrixCommand 标注好的 fallbackMethod 调用类中的指定方法
    @HystrixCommand
    public Dept get(@PathVariable("id") Long id) {
        System.out.println("id = " + id);
        return service.get(id);
    }

    // 备选方法
    public Dept hystrixGet(@PathVariable("id") Long id) {
        return new Dept()
                .setDeptId(id)
                .setDname("id=>" + id)
                .setDbSource("没有数据");
    }

    @RequestMapping("/consumer/dept/list")
    public List<Dept> list() {
        return service.list();
    }
}
