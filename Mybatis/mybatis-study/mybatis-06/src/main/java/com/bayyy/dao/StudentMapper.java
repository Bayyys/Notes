package com.bayyy.dao;

import com.bayyy.pojo.Student;

import java.util.List;

public interface StudentMapper {
    // 查询所有学生信息，以及对应的老师信息
    // 方法一: 按照查询嵌套处理
    public List<Student> getStudent();

    // 查询所有学生信息，以及对应的老师信息
    // 方法二: 按照结果嵌套处理
    public List<Student> getStudent2();
}
