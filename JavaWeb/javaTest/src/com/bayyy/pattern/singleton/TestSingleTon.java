package com.bayyy.pattern.singleton;

public class TestSingleTon {
    public static void main(String[] args) {
        for (int i = 0; i < 10; i++) {
            new Thread(new Runnable() {
                @Override
                public void run() {
                    System.out.println(SingleTon.getInstance().hashCode());
                }
            }).start();
        }
    }
}
