package com.bayyy.pojo;

public class User {
    private String name;

    public User() {
        System.out.println("User 的无参构造方法");
    }

    public User(String name) {
        this.name = name;
        System.out.println("User 的有参构造方法");
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    @Override
    public String toString() {
        return "User{" +
                "name='" + name + '\'' +
                '}';
    }
}
