package com.bayyy.java8.timeapi;

import java.time.LocalDateTime;
import java.time.LocalTime;

public class LocalTimeTest {
    public static void main(String[] args) {
        // 1. 创建本地时间
        LocalDateTime ldt = LocalDateTime.now();
//        LocalDateTime ldt2=LocalDateTime.of(2018, 12, 12, 12, 12, 12);
        System.out.println(ldt);
        System.out.println(ldt.getYear());

        // 2. 添加时间
        LocalDateTime ldt2 = ldt.plusYears(2);
        System.out.println(ldt2);
        LocalDateTime ldt3 = ldt.minusMonths(2);
        System.out.println(ldt3);
    }
}
