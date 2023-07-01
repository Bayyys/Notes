package com.bayyy.pattern.singleton;

/**
 * 饿汉式单例模式
 * 优点：线程安全，调用效率高
 * 缺点：不管用不用都会创建对象，浪费内存
 * 1. 创建一个常量
 * 2. 私有化构造器
 * 3. 提供一个静态方法(获取实例)
 */
public class SingleTon {
    private static final SingleTon INSTANCE = new SingleTon();
    private SingleTon() {}
    public static SingleTon getInstance() {
        return INSTANCE;
    }
}
