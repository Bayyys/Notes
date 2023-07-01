package com.bayyy.cas;

import java.util.concurrent.TimeUnit;
import java.util.concurrent.atomic.AtomicStampedReference;

public class Demo1 {

    //正常的业务，这里面比较的都是一个个对象
    //initialStamp:时间戳
    static AtomicStampedReference<Integer> atomicStampedReference = new AtomicStampedReference<>(1, 1);

    public static void main(String[] args) {

        new Thread(() -> {
            System.out.println("a =>:" + atomicStampedReference.getStamp()+ "当前值为:" + atomicStampedReference.getReference());
            try {
                TimeUnit.SECONDS.sleep(1);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }

            atomicStampedReference.compareAndSet(1, 2, atomicStampedReference.getStamp(), atomicStampedReference.getStamp() + 1);

            System.out.println("a =>:" + atomicStampedReference.getStamp()+ "当前值为:" + atomicStampedReference.getReference());

            atomicStampedReference.compareAndSet(2, 1, atomicStampedReference.getStamp(), atomicStampedReference.getStamp() + 1);

            System.out.println("a =>:" + atomicStampedReference.getStamp()+ "当前值为:" + atomicStampedReference.getReference());

        }, "a").start();


        //和乐观锁的原理相同
        new Thread(() -> {
            int stamp = atomicStampedReference.getStamp();
            System.out.println("b =>:" + stamp+ "当前值为:" + atomicStampedReference.getReference());

            try {
                TimeUnit.SECONDS.sleep(2);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }

            System.out.println(atomicStampedReference.compareAndSet(1, 6, stamp, stamp + 1));

            System.out.println("b =>:" + atomicStampedReference.getStamp()+ "当前值为:" + atomicStampedReference.getReference());
        }, "b").start();
    }
}
