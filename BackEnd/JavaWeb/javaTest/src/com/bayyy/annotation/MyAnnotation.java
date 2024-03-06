package com.bayyy.annotation;

/**
 * 创建注解类型 @interface
 */
public @interface MyAnnotation {
    // 注解的属性(类似接口中的方法
    String name() default "bayyy";

    int age() default 24;
}
