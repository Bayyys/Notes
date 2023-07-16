package com.bayyy.dao;

import com.bayyy.utils.MyBatisUtils;
import org.apache.ibatis.session.SqlSession;
import org.junit.Test;

public class UserMapperTest {
    @Test
    public void testSelectAll() {
        // try-with-resources: try内部的资源会自动释放(且是先声明的资源先释放)
        try (SqlSession sqlSession = MyBatisUtils.getSqlSession()) {
            sqlSession.getMapper(UserMapper.class).getUserList().forEach(System.out::println);
        }
    }
}