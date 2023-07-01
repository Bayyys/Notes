package com.bayyy.cas;

import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public class Demo2 {
    public static void main(String[] args) {
        new Thread(() -> {
            Phone phone = new Phone();
            phone.sms();
        }, "A").start();

        new Thread(() -> {
            Phone phone = new Phone();
            phone.sms();
        }, "B").start();
    }
}

class Phone {
    Lock lock = new ReentrantLock();
    public void sms() {
        lock.lock();
        try {
            System.out.println(Thread.currentThread().getName() + "sms");
            call();
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            lock.unlock();
        }
    }

    public void call() {
        lock.lock();
        try {
            System.out.println(Thread.currentThread().getName() + "call");
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            lock.unlock();
        }
    }
}
