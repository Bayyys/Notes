package com.bayyy.juc;

import java.util.LinkedList;
import java.util.Queue;

public class queueTest {
    public static void main(String[] args) {
        // 1. 创建队列
        // 实现类：LinkedList
        Queue<String> queue = new LinkedList<String>();
        // 2. 入队
        queue.offer("hello");
        queue.offer("world");
        queue.offer("java");
        queue.offer("bayyy");
        // 3. 出队
        System.out.println("元素个数：" + queue.size());
        int size = queue.size();
        for (int i = 0; i < size; i++) {
            System.out.println(queue.peek());
            System.out.println(queue.poll());
        }
        System.out.println("元素个数：" + queue.size());

    }
}
