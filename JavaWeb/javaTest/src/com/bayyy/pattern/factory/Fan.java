package com.bayyy.pattern.factory;

public class Fan implements Usb {
    @Override
    public void service() {
        System.out.println("Fan is working.");
    }
}
