package com.bayyy.service;

import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Service;

import java.text.SimpleDateFormat;
import java.util.Date;

@Service
public class ScheduleService {
    // 秒 分 时 日 月 周几
    @Scheduled(cron = "0/10 52-54 * * * *")
    public void scheduleHello() {
        System.out.println("====================");
        System.out.println("Hello, Scheduling!  "+new SimpleDateFormat("yyyy-MM-dd HH:mm:ss").format(new Date()));
    }
}
