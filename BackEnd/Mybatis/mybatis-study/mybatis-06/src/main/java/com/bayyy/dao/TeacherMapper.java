package com.bayyy.dao;

import com.bayyy.pojo.Teacher;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.annotations.Select;

import java.util.List;

public interface TeacherMapper {
    // 获取老师
    List<Teacher> getTeacher();

    // 获取指定老师下的所有学生及老师信息
    Teacher getTeacherAll(@Param("tid") int id);
    Teacher getTeacherAll2(@Param("tid") int id);
}
