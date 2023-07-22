package com.bayyy.log;


import org.springframework.aop.AfterReturningAdvice;

import java.lang.reflect.Method;

public class AfterLog implements AfterReturningAdvice {
    /*
        * returnValue: 返回值
        * method: 要执行的目标对象的方法
        * args: 参数
        * target: 目标对象
     */
    @Override
    public void afterReturning(Object returnValue, Method method, Object[] args, Object target) throws Throwable {
        System.out.println(target.getClass().getName() + "的" + method.getName() + "方法被执行了, 返回值为:" + returnValue);
    }
}
