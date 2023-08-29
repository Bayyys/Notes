package com.bayyy.springcloud.service;

import com.bayyy.springcloud.pojo.Dept;
import org.springframework.stereotype.Component;

import java.util.List;

@Component
public class DeptClientServiceFallBackFactory implements DeptClientService {
    @Override
    public Dept get(Long id) {
        return new Dept()
                .setDeptId(id)
                .setDname("id=>" + id + "没有对应的信息，客户端提供了降级的信息，这个服务现在已经被关闭")
                .setDbSource("没有数据~");
    }

    @Override
    public List<Dept> list() {
        return null;
    }

    @Override
    public boolean add(Dept dept) {
        return false;
    }
};
