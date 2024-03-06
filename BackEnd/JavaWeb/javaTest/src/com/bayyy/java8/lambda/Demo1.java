package com.bayyy.java8.lambda;

import java.util.Comparator;
import java.util.TreeSet;

public class Demo1 {
    public static void main(String[] args) {
        System.out.println("======Runnable======");
        // 匿名内部类
        Runnable runnable1 = new Runnable() {
            @Override
            public void run() {
                System.out.println("匿名内部类");
            }
        };
        new Thread(runnable1).start();

        // Lambda表达式
        Runnable runnable2 = () -> {
            System.out.println("Lambda表达式");
        };
        new Thread(runnable2).start();

        // Lambda表达式简化
        new Thread(() -> {
            System.out.println("Lambda表达式简化");
        }).start();

        System.out.println("======Comparator======");
        // 匿名内部类
        Comparator<String> com = new Comparator<String>() {
            @Override
            public int compare(String o1, String o2) {
                return o1.length() - o2.length();
            }
        };
        TreeSet<String> treeSet = new TreeSet<>(com);

        // Lambda表达式
        Comparator<String> com2 = (String o1, String o2) -> {
            return o1.length() - o2.length();
        };
        Comparator<String> com3 = (o1, o2) -> o1.length() - o2.length();
        TreeSet<String> treeSet2 = new TreeSet<>(com2);
        TreeSet<String> treeSet3 = new TreeSet<>(com3);

        // Lambda表达式简化
        TreeSet<String> treeSet4 = new TreeSet<>((o1, o2) -> o1.length() - o2.length());
    }
}
