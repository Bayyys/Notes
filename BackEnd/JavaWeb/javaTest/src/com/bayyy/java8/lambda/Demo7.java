package com.bayyy.java8.lambda;

import com.bayyy.annotation.Person;

import java.util.ArrayList;
import java.util.Optional;
import java.util.stream.Collectors;

/**
 * 中间操作
 */
public class Demo7 {
    public static void main(String[] args) {
        ArrayList<Person> list = new ArrayList<>();
        list.add(new Person("张三", 18));
        list.add(new Person("李四", 19));
        list.add(new Person("王五", 20));
        list.add(new Person("赵六", 21));

        // 1. forEach(Consumer c) -- 内部迭代
        list.stream()
                .filter(person -> person.getAge() > 18) // 过滤掉年龄小于18的
                .forEach(System.out::println);

        // 2. min(Comparator c) -- 返回流中最小值
        // 3. max(Comparator c) -- 返回流中最大值
        // 4. count() -- 返回流中元素的总个数
        System.out.println("=====min=====");
        Optional<Person> min = list.stream()
                .min((p1, p2) -> p1.getAge() - p2.getAge());
        System.out.println(min.get());
        System.out.println("=====max=====");
        Optional<Person> max = list.stream()
                .max((p1, p2) -> p1.getAge() - p2.getAge());
        System.out.println(max.get());
        System.out.println("=====count=====");
        long count = list.stream()
                .count();
        System.out.println(count);
        // 5. reduce() -- 可以将流中元素反复结合起来，得到一个值
        // 6. collect() -- 将流转换为其他形式。接收一个 Collector 接口的实现，用于给 Stream 中元素做汇总的方法
        System.out.println("=====reduce=====");
        Optional<Integer> reduce = list.stream()
                .map(Person::getAge)
                .reduce(Integer::sum);  // 求和
        System.out.println(reduce.get());
        System.out.println("=====collect=====");
        list.stream()
                .map(Person::getName)
                .collect(Collectors.toList())
                .forEach(System.out::println);
    }
}
