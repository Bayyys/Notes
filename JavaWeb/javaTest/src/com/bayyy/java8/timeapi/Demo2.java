package com.bayyy.java8.timeapi;

import java.time.Duration;
import java.time.Instant;
import java.time.ZoneId;
import java.util.Set;

public class Demo2 {
    public static void main(String[] args) {
        // 1. Instant
        // 1.1 创建
        Instant ins1 = Instant.now();
        System.out.println(ins1.toString());
        System.out.println(ins1.toEpochMilli());
        // 1.2 添加/减少时间
        Instant ins2 = ins1.plusSeconds(100);
        System.out.println(ins2);
        System.out.println(Duration.between(ins1, ins2).toMillis());

        // 2. ZoneId
        // 2.1 获取所有时区
//         Set<String> set = ZoneId.getAvailableZoneIds();
//         for (String string : set) {
//             System.out.println(string);
//         }
        System.out.println(ZoneId.systemDefault());
    }
}
