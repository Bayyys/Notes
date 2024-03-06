package com.bayyy;

import com.bayyy.pojo.Dog;
import com.bayyy.pojo.Person;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

@SpringBootTest
class Springboot01HelloworldApplicationTests {
    @Autowired
    private Person person;
    @Autowired
    private Dog dog;

    @Test
    void contextLoads() {
        System.out.println(person);
        System.out.println(dog);
    }
}
