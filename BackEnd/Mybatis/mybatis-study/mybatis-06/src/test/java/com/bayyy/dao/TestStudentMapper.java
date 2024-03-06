package com.bayyy.dao;

import com.bayyy.utils.MyBatisUtils;
import org.apache.ibatis.session.SqlSession;
import org.junit.Test;

public class TestStudentMapper {
    @Test
    public void testGetStudent() {
        try (SqlSession sqlSession = MyBatisUtils.getSqlSession()) {
            sqlSession.getMapper(StudentMapper.class).getStudent().forEach(System.out::println);
            sqlSession.getMapper(StudentMapper.class).getStudent2().forEach(System.out::println);
        }
    }
}
