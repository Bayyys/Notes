package com.bayyy.pojo;

import lombok.Data;

import java.util.Date;

@Data
public class Blog {
    private String id;
    private String title;
    private String author;
    private Date   createTime; // 属性名和字段名不一致(通过配置文件解决:mapUnderscoreToCamelCase)
    private int    views;
}
