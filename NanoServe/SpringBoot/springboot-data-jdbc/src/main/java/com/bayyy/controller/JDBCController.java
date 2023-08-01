package com.bayyy.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;
import java.util.Map;

@RestController
public class JDBCController {

    /**
     * Spring Boot 默认提供了数据源，默认提供了 org.springframework.jdbc.core.JdbcTemplate
     * JdbcTemplate 中会自己注入数据源，用于简化 JDBC操作
     * 还能避免一些常见的错误,使用起来也不用再自己来关闭数据库连接
     */
    @Autowired
    JdbcTemplate jdbcTemplate;

    //查询employee表中所有数据
    @GetMapping("/list")
    public List<Map<String, Object>> userList() {
        String sql = "select * from user";
        List<Map<String, Object>> maps = jdbcTemplate.queryForList(sql);
        return maps;
    }

    //新增一个用户
    @GetMapping("/add")
    public String addUser() {
        //插入语句，注意时间问题
        String sql = "insert into user(id, username)" + "values(6,'user3')";
        jdbcTemplate.update(sql);
        //查询
        return "addOk";
    }

    //修改用户信息
    @GetMapping("/update/{id}")
    public String updateUser(@PathVariable("id") int id) {
        //插入语句
        System.out.println(id);
        String sql = "update user set username=? where id=" + id;
        System.out.println(sql);
        //数据
        String username = "user5";
        jdbcTemplate.update(sql, username);
        //查询
        return "updateOk";
    }

    //删除用户
    @GetMapping("/delete/{id}")
    public String delUser(@PathVariable("id") int id) {
        //插入语句
        String sql = "delete from user where id=?";
        jdbcTemplate.update(sql, id);
        //查询
        return "deleteOk";
    }

}
