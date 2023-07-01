package com.bayyy.Internet;

import java.io.IOException;
import java.net.InetAddress;
import java.net.UnknownHostException;

/**
 * 演示 InetAddress 类的使用
 * 1. 创建本机IP地址对象
 * 2， 创建局域网IP地址对象
 * 3. 创建外网IP地址对象
 */
public class InetAddressTest {
    public static void main(String[] args) throws IOException {
        // 1. 创建本机IP地址对象
        // 1.1 getLocalHost()方法
        InetAddress address = InetAddress.getLocalHost();
        System.out.println(address);   // bayyy/192.168.53.5
        System.out.println("ip地址: " + address.getHostAddress() + " 主机名: " + address.getHostName());

        // 1.2 getByName()方法
        InetAddress address2 = InetAddress.getByName("bayyy");
        InetAddress address3 = InetAddress.getByName("192.168.53.5");
        InetAddress address4 = InetAddress.getByName("127.0.0.1");
        InetAddress address5 = InetAddress.getByName("localhost");
        System.out.println("ip地址: " + address2.getHostAddress() + " 主机名: " + address2.getHostName());
        System.out.println("ip地址: " + address3.getHostAddress() + " 主机名: " + address3.getHostName());
        System.out.println("ip地址: " + address4.getHostAddress() + " 主机名: " + address4.getHostName());
        System.out.println("ip地址: " + address5.getHostAddress() + " 主机名: " + address5.getHostName());


        // 2. 创建局域网IP地址对象
        // 静态方法：getByName(String host)
        InetAddress ia1 = InetAddress.getByName("192.168.53.4");
//        System.out.println("ip地址: " + ia1.getHostAddress() + " 主机名: " + ia1.getHostName());
        if (ia1.isReachable(1000)) {    // 判断是否可以连通
            System.out.println("可以ping通");
        } else {
            System.out.println("不可以ping通");
        }

        // 3. 创建外网IP地址对象
        InetAddress ia2 = InetAddress.getByName("www.baidu.com");   // 通过域名创建
        System.out.println("ip地址: " + ia2.getHostAddress() + " 主机名: " + ia2.getHostName());
        InetAddress[] ias = InetAddress.getAllByName("www.baidu.com");  // 获取所有的IP地址
        for (InetAddress ia : ias) {
            System.out.println("ip地址: " + ia.getHostAddress() + " 主机名: " + ia.getHostName());

        }
        if (ia2.isReachable(1000)) {
            System.out.println("可以ping通");
        } else {
            System.out.println("不可以ping通");
        }


    }
}
