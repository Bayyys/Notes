package com.bayyy.java8.lambda;

import com.bayyy.annotation.Person;

import java.util.ArrayList;

/**
 * 中间操作
 */
public class Demo6 {
    public static void main(String[] args) {
        ArrayList<Person> list = new ArrayList<>();
        list.add(new Person("张三", 18));
        list.add(new Person("李四", 19));
        list.add(new Person("王五", 20));
        list.add(new Person("赵六", 21));
        list.add(new Person("田七", 22));
        System.out.println("====1====");
        // 1. filter(Predicate p) -- 接收 Lambda， 从流中排除某些元素
        // 2. limit(n) -- 截断流，使其元素不超过给定数量
        // 3. skip(n) -- 跳过元素，返回一个扔掉了前 n 个元素的流。若流中元素不足 n 个，则返回一个空流。与 limit(n) 互补
        // 4. distinct() -- 筛选，通过流所生成元素的 hashCode() 和 equals() 去除重复元素
        list.stream()
                .filter(person -> person.getAge() > 18) // 过滤掉年龄小于18的
                .limit(4)   // 只取前4个
                .skip(1)    // 跳过第一个
                .distinct() // 去重
                .forEach(System.out::println);  // 遍历

        System.out.println("====2====");
        // 5. sorted() -- 自然排序
        list.stream()
                .sorted((p1, p2) -> p1.getAge() - p2.getAge())
                .forEach(System.out::println);
        System.out.println("====3====");
        // 6. map(Function f) -- 接收 Lambda，将元素转换成其他形式或提取信息。接收一个函数作为参数，该函数会被应用到每个元素上，并将其映射成一个新的元素
        // 7. flatMap(Function f) -- 接收一个函数作为参数，将流中的每个值都换成另一个流，然后把所有流连接成一个流
        list.stream().map(Person::getName).forEach(System.out::println);

        System.out.println("====4====");
        // 8. parallel() -- 返回一个并行流(多线程)
        list.parallelStream()
                .forEach(System.out::println);
    }
}
