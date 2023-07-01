package com.bayyy.pattern.factory;

public class Mouse implements Usb{

    @Override
    public void service() {
        System.out.println("Mouse is working.");
    }
}
