package com.bayyy.demo1;

public class Client {
    public static void main(String[] args) {
//        Host host = new Host();
//        Proxy proxy = new Proxy(host);
//        proxy.rent();
//        // 代理, 代理角色一般会有一些附属操作!
//        proxy.seeHouse();
//        proxy.fee();
//        proxy.signContract();
        // 真实角色
        Host host = new Host();

        // 代理角色
        ProxyInvocationHandler proxyInvocationHandler = new ProxyInvocationHandler();
        proxyInvocationHandler.setRent(host);
        Rent proxy = (Rent) proxyInvocationHandler.getProxy();
        proxy.rent();
    }
}
