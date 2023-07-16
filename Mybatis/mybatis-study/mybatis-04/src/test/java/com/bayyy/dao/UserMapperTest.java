package com.bayyy.dao;

import com.bayyy.pojo.User;
import com.bayyy.utils.MyBatisUtils;
import org.apache.ibatis.session.SqlSession;
import org.junit.Test;

public class UserMapperTest {
    @Test
    public void testSelectAll() {
        // try-with-resources: try内部的资源会自动释放(且是先声明的资源先释放)
        try (SqlSession sqlSession = MyBatisUtils.getSqlSession()) {
            UserMapper mapper = sqlSession.getMapper(UserMapper.class);
            mapper.getUserList().forEach(System.out::println);
        }
    }

    @Test
    public void testSelectById() {
        try (SqlSession sqlSession = MyBatisUtils.getSqlSession()) {
            System.out.println(sqlSession.getMapper(UserMapper.class).getUserById(1));
        }
    }

    @Test
    public void testAddUser() {
        try (SqlSession sqlSession = MyBatisUtils.getSqlSession()) {
            sqlSession.getMapper(UserMapper.class).addUser(new User(5, "长江五号", "123456"));
            // openSession(true) 会自动提交事务
        }
    }

    @Test
    public void testUpdate() {
        try (SqlSession sqlSession = MyBatisUtils.getSqlSession()) {
            sqlSession.getMapper(UserMapper.class).updateUser(new User(5, "长江五号", ""));
            System.out.println(sqlSession.getMapper(UserMapper.class).getUserById(5));
        }
    }

    @Test
    public void testDelete() {
        try (SqlSession sqlSession = MyBatisUtils.getSqlSession()) {
            sqlSession.getMapper(UserMapper.class).deleteUser(5);
            sqlSession.getMapper(UserMapper.class).getUserList().forEach(System.out::println);
        }
    }
}