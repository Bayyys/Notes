package com.bayyy.pojo;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Component;

@Component
public class Dog {
    @Value("小白")
    public String name;

    public String getName() {
        return name;
    }
}
