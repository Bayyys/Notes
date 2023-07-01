package com.bayyy.java8.lambda;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Random;
import java.util.stream.IntStream;
import java.util.stream.Stream;

/**
 * Stream API 的使用
 * 1. Stream API 的特点
 * ① Stream 自己不会存储元素
 * ② Stream 不会改变源对象。相反，他们会返回一个持有结果的新Stream
 * ③ Stream 操作是延迟执行的。这意味着他们会等到需要结果的时候才执行
 * ④ Stream API 是在 JDK 8 中引入的，是对集合对象功能的增强
 * ⑥ Stream API 是一个抽象层，它使用一种类似用 SQL 语句从数据库查询数据的直观方式来提供一种对 Java 集合运算和表达的高阶抽象
 * ⑦ Stream API 可以对集合数据进行各种操作。例如：filter(过滤)、map(映射)、limit(限制)、sorted(排序)、collect(收集)等
 * 2. Stream API 执行流程
 * ① Stream 的实例化
 * ② 一系列的中间操作（过滤、映射、...）
 * ③ 终止操作
 * 3. Stream 的创建
 * ① 通过集合(Collection)对象的 stream() 或 parallelStream() 方法创建
 * ② 通过 Arrays 中的 stream() 方法获取数组流
 * ③ 通过 Stream 类中的静态方法 of(), iterate(), generate() 创建
 * ④ 创建 IntStream、LongStream、DoubleStream接口中的of,range,rangeClosed方法
 */
public class Demo5 {
    public static void main(String[] args) {
        // 1. 通过集合(Collection)对象的 stream() 或 parallelStream() 方法创建
        ArrayList<String> list = new ArrayList<>();
        list.add("hello");
        list.add("world");
        list.add("java");
        Stream<String> stream = list.stream();
        Stream<String> stringStream = list.parallelStream();
        // 遍历
        stream.forEach(System.out::println);
        stringStream.forEach(System.out::println);

        // 2. 通过 Arrays 中的 stream() 方法获取数组流
        String[] arr=new String[]{"hello","world","java"};
        Stream<String> stream1 = Arrays.stream(arr);
        stream1.forEach(System.out::println);

        // 3. 通过 Stream 类中的静态方法 of(), iterate(), generate() 创建
        // 3.1 of()方法
        Stream<Integer> stream2 = Stream.of(1, 2, 3, 4, 5);
        stream2.forEach(System.out::println);
        // 3.2 iterate()方法
        Stream<Integer> stream3 = Stream.iterate(0, x -> x + 2).limit(10);
        stream3.forEach(System.out::println);
        // 3.3 generate()方法
        Stream<Double> stream4 = Stream.generate(() -> new Random().nextDouble(100)).limit(2);
        stream4.forEach(System.out::println);

        // 4. 创建 IntStream、LongStream、DoubleStream接口中的of,range,rangeClosed方法
        // 4.1 of()方法
        IntStream.of(new int[]{1, 2, 3}).forEach(System.out::println);
        // 4.2 range()方法
        IntStream.range(1, 3).forEach(System.out::println);
        // 4.3 rangeClosed()方法
        IntStream.rangeClosed(1, 3).forEach(System.out::println);
    }
}
