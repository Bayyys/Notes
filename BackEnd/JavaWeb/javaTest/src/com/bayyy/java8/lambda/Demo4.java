package com.bayyy.java8.lambda;

import com.bayyy.annotation.Person;

import java.util.Comparator;
import java.util.function.Consumer;
import java.util.function.Function;
import java.util.function.Supplier;

/**
 * 方法引用的使用
 * 使用情景：当要传递给Lambda体的操作，已经有实现的方法了，可以使用方法引用！
 * 1. 对象::实例方法名
 * 2. 类::静态方法名
 * 3. 类::实例方法名
 * 4. 类::new
 * 注意：Lambda体中调用方法的参数列表与返回值类型，要与函数式接口中抽象方法的函数列表和返回值类型保持一致！
 */
public class Demo4 {
    public static void main(String[] args) {
        // 1. 对象::实例方法名
        Consumer<String> consumer = s -> System.out.println(s);
        consumer.accept("hello");
        Consumer<String> consumer2 = System.out::println;
        consumer2.accept("hello");

        // 2. 类::静态方法名
        Comparator<Integer> com = (x, y) -> Integer.compare(x, y);
        Comparator<Integer> com2 = Integer::compare;

        // 3. 类::实例方法名
        Function<Person, String> function = person -> person.getName();
        Function<Person, String> function2 = Person::getName;

        // 4. 类::new
        Supplier<Person> supplier = () -> new Person("bayyy", 18);
        Supplier<Person> supplier2 = Person::new;
    }
}
