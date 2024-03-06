package com.bayyy.pojo;


import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.util.List;

@Data
public class Teacher {
    private int id;
    private String name;
    // 一个老师拥有多个学生
    private List<Student> students;
}
