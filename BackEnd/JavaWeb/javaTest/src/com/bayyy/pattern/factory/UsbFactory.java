package com.bayyy.pattern.factory;

public class UsbFactory {
    public static Usb createUsb(int type) {
        if (type == 1) {
            return new Upan();
        } else if (type == 2) {
            return new Mouse();
        } else if (type == 3) {
            return new Upan();
        }
        return null;
    }

    public static Usb createUsb(String type) {
        Usb usb = null;
        Class<?> class1 = null;
        try {
            class1 = Class.forName(type);
            usb = (Usb) class1.newInstance();
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
        return usb;
    }
}
