package com.bayyy.dao;

import com.bayyy.utils.MyBatisUtils;
import org.apache.ibatis.session.SqlSession;
import org.junit.Test;

public class TestTeacherMapper {
    @Test
    public void test() {
        try (SqlSession sqlSession = MyBatisUtils.getSqlSession()){
            System.out.println(sqlSession.getMapper(TeacherMapper.class).getTeacher(1));
        }
    }
}
