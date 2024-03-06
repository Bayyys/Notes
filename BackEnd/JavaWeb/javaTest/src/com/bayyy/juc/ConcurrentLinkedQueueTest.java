package com.bayyy.juc;

import java.util.concurrent.ConcurrentLinkedQueue;

public class ConcurrentLinkedQueueTest {
    public static void main(String[] args) {
        // 1. 创建队列
        // 实现类：ConcurrentLinkedQueue
        ConcurrentLinkedQueue<String> queue = new ConcurrentLinkedQueue<String>();
        // 2. 创建线程
        Thread t1 = new Thread(new Runnable() {
            @Override
            public void run() {
                for (int i = 0; i < 10; i++) {
                    queue.offer("hello" + i);
                }
            }
        });
        Thread t2 = new Thread(new Runnable() {
            @Override
            public void run() {
                for (int i = 0; i < 10; i++) {
                    queue.offer("world" + i);
                }
            }
        });
        // 3. 线程启动
        t1.start();
        t2.start();
        // 4. 等待线程执行完毕
        try {
            t1.join();
            t2.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        // 5. 遍历队列
        System.out.println("元素个数：" + queue.size());
        int size = queue.size();
        for (int i = 0; i < size; i++) {
            System.out.println(queue.peek());
            System.out.println(queue.poll());
        }
        System.out.println("元素个数：" + queue.size());
    }
}
