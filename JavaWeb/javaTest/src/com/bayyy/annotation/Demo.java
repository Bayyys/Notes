package com.bayyy.annotation;

import java.lang.reflect.Method;

public class Demo {
    public static void main(String[] args) throws Exception {
        // 1. 获取类对象
        Class<?> class1 = Class.forName("com.bayyy.annotation.Person");
        // 2. 获取方法对象
        Method method = class1.getMethod("test4", String.class, int.class, String.class);
        // 3. 获取方法上的注解
        PersonInfo personInfo = method.getAnnotation(PersonInfo.class);
        // 4. 获取注解上的属性值
        String name = personInfo.name();
        int age = personInfo.age();
        String sex = personInfo.sex();
        System.out.println(name+"==="+age+"==="+sex);
    }
}
