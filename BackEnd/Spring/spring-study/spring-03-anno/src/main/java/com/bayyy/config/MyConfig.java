package com.bayyy.config;

import com.bayyy.pojo.Dog;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;

@Configuration
@ComponentScan("com.bayyy.pojo")
public class MyConfig {
    @Bean
    public Dog getDog() {
        return new Dog();
    }
}
