package com.bayyy.pojo;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Component;

// 等价于 <bean id="user" class="com.bayyy.pojo.User"/>
// @Component 组件
@Component("user")
public class User {
    public String name;

    @Value("Bayyy")
    public void setName(String name) {
        this.name = name;
    }
}
