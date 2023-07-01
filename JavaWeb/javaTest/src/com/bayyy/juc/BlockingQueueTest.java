package com.bayyy.juc;

import java.util.concurrent.ArrayBlockingQueue;
import java.util.concurrent.BlockingQueue;
import java.util.concurrent.LinkedBlockingQueue;

public class BlockingQueueTest {
    public static void main(String[] args) {
        // 1. 创建队列
        // 实现类：ArrayBlockingQueue、LinkedBlockingQueue、PriorityBlockingQueue
        BlockingQueue<String> queue1=new ArrayBlockingQueue<String>(3);
        BlockingQueue<String> queue2=new LinkedBlockingQueue<String>();
        // 2. 添加元素
        queue1.offer("hello");
        queue1.offer("world");
        queue1.offer("java");
        // 3. 阻塞式添加元素
        try {
            queue1.put("bayyy");
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        // 4. 阻塞式获取元素
        try {
            System.out.println(queue1.take());
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}
