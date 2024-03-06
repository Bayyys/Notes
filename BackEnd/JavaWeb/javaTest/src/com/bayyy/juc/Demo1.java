package com.bayyy.juc;

import java.util.concurrent.CompletableFuture;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.TimeUnit;

/**
 * 测试 异步调用 CompletableFuture
 */
public class Demo1 {
    public static void main(String[] args) throws ExecutionException, InterruptedException {
        test2();
    }

    private static void test1() {
        // future
        CompletableFuture<Void> completableFuture = CompletableFuture.runAsync(() -> {
            try {
                TimeUnit.SECONDS.sleep(2);
            } catch (InterruptedException e) {
                throw new RuntimeException(e);
            }
            System.out.println(Thread.currentThread().getName() + " runAsync=>Void");
        });

        try {
            completableFuture.get();
        } catch (InterruptedException | ExecutionException e) {
            throw new RuntimeException(e);
        }
    }

    private static void test2() throws ExecutionException, InterruptedException {
        CompletableFuture<Integer> cf = CompletableFuture.supplyAsync(() -> {
            System.out.println(Thread.currentThread().getName() + " supplyAsync=>Integer");
            int i = 10 / 0;
            return 1024;
        });

        System.out.println(cf.whenComplete((t, u) -> {
            System.out.println("t=>" + t);  // 正常的返回结果
            System.out.println("u=>" + u);  // 错误信息
        }).exceptionally((e) -> {
            System.out.println(e.getMessage());
            return 233;
        }).get());
    }
}
