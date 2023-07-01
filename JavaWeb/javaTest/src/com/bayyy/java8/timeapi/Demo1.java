package com.bayyy.java8.timeapi;

import java.text.SimpleDateFormat;
import java.time.LocalTime;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;
import java.util.concurrent.Callable;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;

public class Demo1 {
    public static void main(String[] args) {
        DateTimeFormatter dtf = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
        ExecutorService pool = Executors.newFixedThreadPool(10);
        Callable<LocalTime> callable = new Callable<LocalTime>() {
            @Override
            public LocalTime call() throws Exception {
                return LocalTime.parse("2018-12-12 12:12:12", dtf);
            }
        };
        List<Future<LocalTime>> list = new ArrayList<>();
        for (int i = 0; i < 10; i++) {
            Future<LocalTime> future = pool.submit(callable);
            list.add(future);
        }
        for (Future<LocalTime> future : list) {
            try {
                System.out.println(future.get());
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
        pool.shutdown();
    }
}
