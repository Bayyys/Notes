package com.bayyy.java8.timeapi;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class Demo4 {
    public static void main(String[] args) {
        DateTimeFormatter dtf = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
//        DateTimeFormatter dtf2 = DateTimeFormatter.ISO_LOCAL_DATE_TIME;
        // 1. 把时间格式化为字符串
        System.out.println(dtf.format(LocalDateTime.now()));
        // 2. 把字符串解析为时间
        System.out.println(LocalDateTime.parse("2018-12-12 12:12:12", dtf));
    }
}
