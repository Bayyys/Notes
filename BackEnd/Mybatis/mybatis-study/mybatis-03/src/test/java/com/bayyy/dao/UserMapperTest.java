package com.bayyy.dao;

import com.bayyy.utils.MyBatisUtils;
import org.apache.ibatis.session.RowBounds;
import org.apache.ibatis.session.SqlSession;
import org.apache.log4j.Logger;
import org.junit.Test;

import java.util.HashMap;
import java.util.Map;

public class UserMapperTest {
    static Logger logger = Logger.getLogger(UserMapperTest.class);

    @Test
    public void testLog4j() {
        logger.info("info:进入了testLog4j");
        logger.debug("debug:进入了testLog4j");
        logger.error("error:进入了testLog4j");
    }

    @Test
    public void testSelectAll() {
        // try-with-resources: try内部的资源会自动释放(且是先声明的资源先释放)
        try (SqlSession sqlSession = MyBatisUtils.getSqlSession()) {
            sqlSession.getMapper(UserMapper.class).getUserList().forEach(System.out::println);
        }
    }

    @Test
    public void testSelectById() {
        try (SqlSession sqlSession=MyBatisUtils.getSqlSession()){
            System.out.println(sqlSession.getMapper(UserMapper.class).getUserById(1));
        }
    }

    @Test
    public void testGetUserByLimit() {
        try (SqlSession sqlSession=MyBatisUtils.getSqlSession()){
            HashMap<Object, Integer> map = new HashMap<Object, Integer>();
            map.put("startIndex", 0);
            map.put("pageSize", 2);
            sqlSession.getMapper(UserMapper.class).getUserByLimit(map).forEach(System.out::println);
        }
    }

    @Test
    public void testGetUserByRowBounds() {
        try (SqlSession sqlSession=MyBatisUtils.getSqlSession()){
            // RowBounds实现
            RowBounds rowBounds = new RowBounds(1, 2);
            sqlSession.selectList("com.bayyy.dao.UserMapper.getUserByRowBounds", null, rowBounds).forEach(System.out::println);
        }
    }
}