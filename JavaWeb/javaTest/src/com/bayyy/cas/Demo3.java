package com.bayyy.cas;

import java.util.concurrent.TimeUnit;
import java.util.concurrent.atomic.AtomicReference;

public class Demo3 {
    public static void main(String[] args) {
        MySpinLock mySpinLock = new MySpinLock();

        //线程T1，原来没有锁，现在加锁。等待5秒后，解锁
        new Thread(() -> {
            mySpinLock.myLock();
            try {
                TimeUnit.SECONDS.sleep(5);
            } catch (InterruptedException e) {
                e.printStackTrace();
            } finally {
                mySpinLock.myUnLock();
            }
        }, "T1").start();

        //线程T2，原来没有锁。现在加锁，因为都是同一把锁，要上面的锁解了，才能接现在的锁
        new Thread(() -> {
            mySpinLock.myLock();
            try {
                TimeUnit.SECONDS.sleep(1);
            } catch (InterruptedException e) {
                e.printStackTrace();
            } finally {
                mySpinLock.myUnLock();
            }
        }, "T2").start();
    }
}

//我的自旋锁
class MySpinLock {
    /**
     * int 0
     * Thread null
     */
    AtomicReference<Thread> atomicReference = new AtomicReference<>();

    //加锁
    public void myLock() {
        Thread thread = Thread.currentThread();
        System.out.println(Thread.currentThread().getName() + "==>MyLock");

        //自旋锁(如果没有锁，给他加锁。如果有锁，进入方法体)
        while (!atomicReference.compareAndSet(null, thread)) {

        }
    }

    //解锁
    public void myUnLock() {
        Thread thread = Thread.currentThread();
        System.out.println(Thread.currentThread().getName() + "==>myUnlock");
        atomicReference.compareAndSet(thread, null);
    }
}
