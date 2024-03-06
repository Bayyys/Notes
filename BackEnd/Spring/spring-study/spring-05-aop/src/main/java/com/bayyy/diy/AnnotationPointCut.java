package com.bayyy.diy;

import org.aspectj.lang.ProceedingJoinPoint;
import org.aspectj.lang.annotation.After;
import org.aspectj.lang.annotation.Around;
import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.Before;

@Aspect
public class AnnotationPointCut {
    @Before("execution(* com.bayyy.service.UserServiceImpl.*(..))")
    public void before() {
        System.out.println("====== method before ======");
    }

    @After("execution(* com.bayyy.service.UserServiceImpl.*(..))")
    public void after() {
        System.out.println("====== method after ======");
    }

    @Around("execution(* com.bayyy.service.UserServiceImpl.*(..))")
    public void round(ProceedingJoinPoint jp) throws Throwable {
        System.out.println("====== method around before ======");
        Object proceed = jp.proceed();  // 如果不执行这个方法，业务层的方法就不会被执行
        System.out.println("signature: " + jp.getSignature());
        System.out.println("====== method around after ======");
    }
}
