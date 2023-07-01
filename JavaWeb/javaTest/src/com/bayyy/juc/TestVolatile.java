package com.bayyy.juc;

public class TestVolatile {
    private volatile static int num = 0;
//    private static int num = 0;

    public static void main(String[] args) {
//        test1();
        test2();
    }

    /**
     * volatile 保证可见性
     */
    private static void test1() {
        new Thread(() -> {
            while (num == 0) {

            }
        }, "t1").start();

        try {
            Thread.sleep(2);
            num = 1;
            System.out.println("num => " + num);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

    private synchronized static void add() {
        num++;
    }

    /**
     * volatile 不保证原子性
     */
    private static void test2() {
        for (int i = 0; i < 20; i++) {
            new Thread(() -> {
                for (int j = 0; j < 1000; j++) {
                    add();
                }
            }, String.valueOf(i)).start();
        }

        while (Thread.activeCount() > 2) {
            Thread.yield();
        }

        System.out.println("num => " + num);
    }
}
