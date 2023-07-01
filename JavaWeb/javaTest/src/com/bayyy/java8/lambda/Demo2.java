package com.bayyy.java8.lambda;

public class Demo2 {
    public static void main(String[] args) {
        // 匿名内部类
        Usb mouse = new Usb() {
            @Override
            public void service() {
                System.out.println("鼠标开始工作了....");
            }
        };

        Usb fan=() -> System.out.println("风扇开始工作了....");

        run(mouse);
        run(fan);

    }

    private static void run(Usb usb) {
        usb.service();
    }
}
