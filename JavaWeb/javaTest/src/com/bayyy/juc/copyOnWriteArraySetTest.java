package com.bayyy.juc;

import java.util.concurrent.CopyOnWriteArraySet;

public class copyOnWriteArraySetTest {
    public static void main(String[] args) {
        // 1. 创建集合对象
        CopyOnWriteArraySet<String> set=new CopyOnWriteArraySet<String>();
        // 2. 添加元素
        set.add("hello");
        set.add("world");
        set.add("java");
        set.add("bayyy");
        // 3. 遍历集合
        for (String s : set) {
            System.out.println(s);
        }
        System.out.println("---------");
        System.out.println("元素个数："+set.size());
        System.out.println(set.toString());

    }
}
