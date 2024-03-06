package com.bayyy.dao;

import com.bayyy.pojo.Teacher;
import com.bayyy.utils.MyBatisUtils;
import org.apache.ibatis.session.SqlSession;
import org.junit.Test;

public class TestTeacherMapper {
    @Test
    public void testGetTeacher() {
        try (SqlSession sqlSession = MyBatisUtils.getSqlSession()) {
//            sqlSession.getMapper(TeacherMapper.class).getTeacher().forEach(System.out::println);
//            Teacher teacherAll = sqlSession.getMapper(TeacherMapper.class).getTeacherAll(1);
            Teacher teacherAll = sqlSession.getMapper(TeacherMapper.class).getTeacherAll2(1);
            System.out.println(teacherAll);
        }
    }

}
