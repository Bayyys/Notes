package com.bayyy.springcloud.service;

import com.bayyy.springcloud.pojo.Dept;
import org.springframework.cloud.openfeign.FeignClient;
import org.springframework.stereotype.Component;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;

import java.util.List;

@Component
@FeignClient(value = "springcloud-provider-dept", fallback = DeptClientServiceFallBackFactory.class)
public interface DeptClientService {
    @GetMapping("/dept/add")
    public boolean add(Dept dept);

    @GetMapping("/dept/get/{id}")

    public Dept get(@PathVariable("id") Long id);

    @GetMapping("/dept/list")

    public List<Dept> list();
}
