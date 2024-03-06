package com.bayyy.diy;

import org.aspectj.lang.ProceedingJoinPoint;
import org.aspectj.lang.annotation.Around;

public class DiyPointCut {
    public void before() {
        System.out.println("====== method before ======");
    }

    public void after() {
        System.out.println("====== method after ======");
    }


}
