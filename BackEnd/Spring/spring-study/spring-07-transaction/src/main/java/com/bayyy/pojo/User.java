package com.bayyy.pojo;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.stereotype.Component;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Component("user")
public class User {
    @Value("5")
    private int id;
    @Value("长江四号")
    private String name;
    @Value("123456")
    private String pwd;
}
