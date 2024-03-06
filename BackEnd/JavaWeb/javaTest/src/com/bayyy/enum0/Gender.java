package com.bayyy.enum0;

/**
 * 性别枚举类
 * 1. 枚举类的本质是什么？    类
 * 2. 枚举类的构造器默认是私有的
 * 3. 枚举中必须要包含枚举常量，也可以包含其他的属性和方法
 * 4， 枚举常量必须在前面，多个常量之间用逗号隔开，最后分号可写可不写
 */
public enum Gender {
    Male, FEMALE;
    private String name;    // 可以包含其他的属性

    private Gender() {
    } // 可以包含构造器

    public static void show2() {
    } // 可以包含静态方法

    public void show1() {
    } // 可以包含方法
}
