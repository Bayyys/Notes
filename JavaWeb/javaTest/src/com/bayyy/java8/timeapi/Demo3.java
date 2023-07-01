package com.bayyy.java8.timeapi;

import java.time.Instant;
import java.time.LocalDateTime;
import java.time.ZoneId;
import java.util.Date;

public class Demo3 {
    public static void main(String[] args) {
        // 1. Date -> Instant -> LocalDateTime
        Date date = new Date();
        Instant ins = date.toInstant();
        System.out.println(ins);
        LocalDateTime ldt = LocalDateTime.ofInstant(ins, ZoneId.systemDefault());
        System.out.println(ldt);

        // 2. LocalDateTime -> Instant -> Date
        Instant ins2 = ldt.atZone(ZoneId.systemDefault()).toInstant();
        Date date2 = Date.from(ins2);
        System.out.println(date2);
        System.out.println(date2);
    }
}
