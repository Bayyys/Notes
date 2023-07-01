package com.bayyy.Reflection;

public class Person {
    private String name;
    private int age;
    private String address;

    public  void eat() {
        System.out.println(name+" is eating.");
    }

    public void eat(String food) {
        System.out.println(name+" is eating "+food+".");
    }

    private void privateMethod() {
        System.out.println("This is a private method.");
    }


    public static void staticMethod() {
        System.out.println("This is a static method.");
    }

    public Person() {
    }

    public Person(String name, int age, String address) {
        this.name = name;
        this.age = age;
        this.address = address;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    @Override
    public String toString() {
        return "Person{" +
                "name='" + name + '\'' +
                ", age=" + age +
                ", address='" + address + '\'' +
                '}';
    }

}
