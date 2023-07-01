package com.bayyy.java8.lambda;

import java.util.function.Consumer;

public class Demo3 {
    public static void main(String[] args) {
        Consumer<Double> consumer=new Consumer<Double>() {
            @Override
            public void accept(Double aDouble) {
                System.out.println("消费了"+aDouble+"元");
            }
        };
        happy(consumer,1000.0);

        Consumer<Double> consumer2=money-> System.out.println("消费了"+money+"元");
        happy(consumer2,1000.0);
        happy(money-> System.out.println("消费了"+money+"元"),1000.0);

    }
    public static void happy(Consumer<Double> consumer, double money) {
        consumer.accept(money);
    }
}
