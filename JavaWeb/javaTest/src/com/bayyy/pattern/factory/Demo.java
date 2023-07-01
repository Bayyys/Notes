package com.bayyy.pattern.factory;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.Properties;
import java.util.Scanner;

/**
 * 客户程序
 */
public class Demo {
    public static void main(String[] args) {
        System.out.println("Factory Pattern Demo.");
        System.out.println("=======请选择创建的产品类型 1 鼠标 2 风扇 3 U盘=======");
        // 1=com.bayyy.pattern.factory.Mouse
        // 2=com.bayyy.pattern.factory.Fan
        // 3=com.bayyy.pattern.factory.Upan
        Properties properties=new Properties();
        try {
            FileInputStream fis=new FileInputStream("D:\\Coding\\test\\javaTest\\src\\com\\bayyy\\pattern\\factory\\usb.properties");
            properties.load(fis);
            fis.close();
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
        Scanner input=new Scanner(System.in);
        String choice=input.next();
        Usb usb=UsbFactory.createUsb(properties.getProperty(choice));
//        Usb usb=UsbFactory.createUsb(choice);
        if(usb!=null){
            System.out.println("产品创建成功");
            usb.service();
        } else {
            System.out.println("产品创建失败!");
        }
    }
}
