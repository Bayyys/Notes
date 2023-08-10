package com.bayyy;

import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.baomidou.mybatisplus.core.conditions.update.UpdateWrapper;
import com.baomidou.mybatisplus.extension.plugins.pagination.Page;
import com.bayyy.dao.UserMapper;
import com.bayyy.pojo.User;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

import java.sql.Wrapper;
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
        for (int i = 0; i < 10_0000; i++) {
            User user = new User();
            user.setName("Bayyy"+i);
            user.setAge(i);
            user.setEmail("110@011.com");
            userMapper.insert(user);
        }
    }

    @Test
    void testUpdate() {
        UpdateWrapper<User> wrapper = new UpdateWrapper<>();
        wrapper.eq("email", "") // email = ""
                .set("email", null); // set email = null
        userMapper.update(null, wrapper);
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

    @Test
    void testPage() {
        Page<User> page = new Page<>(1, 5);
        userMapper.selectPage(page, null);
        List<User> userList = page.getRecords();
        userList.forEach(System.out::println);
    }

    @Test
    void testDelete() {
//        userMapper.selectList(null).forEach(System.out::println);
        // 根据id删除
        userMapper.deleteById(1);
        // 根据id批量删除
        userMapper.deleteBatchIds(Arrays.asList(20, 21, 22));
        // 条件删除
        HashMap<String, Object> map = new HashMap<>();
        map.put("name", "Bayyy");
        map.put("id", 23);
        userMapper.deleteByMap(map);
    }

    @Test
    void testGE() {
        QueryWrapper<User> wrapper = new QueryWrapper<>();
        wrapper.ge("age", 20)  // age >= 20
                .lt("age", 100) // age < 100
                .isNotNull("name") // name 非空
                .isNull("email"); // email 为空
        userMapper.selectList(wrapper).forEach(System.out::println);
    }

    @Test
    void testLike() {
        QueryWrapper<User> wrapper = new QueryWrapper<>();
        wrapper.likeLeft("age", 2) // age like "%2"
                .in("name", new String[]{"Bayyy", "Bayyy2"}) // name in ("Bayyy", "Bayyy2")
                .notIn("id", new Integer[]{1, 2, 3}); // id not in (1, 2, 3)
        userMapper.selectList(wrapper).forEach(System.out::println);
    }

    @Test
    void testSql() {
        QueryWrapper<User> wrapper = new QueryWrapper<>();
        wrapper.inSql("id", "select id from user where id < 30") // id in (select id from user where id < 30
                .notInSql("age", "select age from user where age < 30 and age > 3"); // age not in (select age from user where age < 30 and age > 3)
        userMapper.selectList(wrapper).forEach(System.out::println);
    }
}