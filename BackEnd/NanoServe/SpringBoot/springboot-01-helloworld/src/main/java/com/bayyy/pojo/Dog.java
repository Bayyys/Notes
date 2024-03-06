package com.bayyy.pojo;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.PropertySource;
import org.springframework.stereotype.Component;

@Component
@Data
@NoArgsConstructor
@AllArgsConstructor
@PropertySource(value = "classpath:dog.properties")
public class Dog {
    // SPEL表达式读取配置文件中的值
    @Value("${dog.name}")
    private String name;
    @Value("${dog.age}")
    private Integer age;
}
