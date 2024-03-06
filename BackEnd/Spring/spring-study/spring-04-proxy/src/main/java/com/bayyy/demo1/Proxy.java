package com.bayyy.demo1;

public class Proxy implements Rent{
    private Host host;
    public Proxy() {
    }
    public Proxy(Host host) {
        this.host = host;
    }

    public void seeHouse() {
        System.out.println("see house");
    }

    public void fee() {
        System.out.println("fee");
    }

    public void signContract() {
        System.out.println("sign contract");
    }

    @Override
    public void rent() {
        host.rent();
    }
}
