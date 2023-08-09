package com.bayyy;

import com.bayyy.dao.UserMapper;
import com.bayyy.pojo.User;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;

@SpringBootTest
class MybatisPlusApplicationTests {
    @Autowired
    private UserMapper userMapper;

    @Test
    void contextLoads() {
        userMapper.selectList(null).forEach(System.out::println);
    }

    @Test
    void testInsert() {
        User user = new User();
        user.setName("Bayyy");
        user.setAge(20);
        user.setEmail("110@011.com");
        userMapper.insert(user);
        System.out.println(user);
    }

    @Test
    void testUpdate() {
        User user = userMapper.selectById(1);
        user.setName("Bayyy_version");
        userMapper.updateById(user);
        System.out.println(user);
    }

    @Test
    void testSelect() {
//        List<User> users = userMapper.selectBatchIds(Arrays.asList(1, 2, 3));
//        users.forEach(System.out::println);
        // 测试条件查询
        HashMap<String, Object> map = new HashMap<>();
        map.put("name", "Bayyy");
        List<User> userList = userMapper.selectByMap(map);
        userList.forEach(System.out::println);
    }

}
