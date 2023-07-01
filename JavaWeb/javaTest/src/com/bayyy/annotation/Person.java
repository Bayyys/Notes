package com.bayyy.annotation;

public class Person {
    private String name;
    private int age;

    public Person() {

    }

    public int getAge() {
        return age;
    }

    @Override
    public String toString() {
        return "Person{" +
                "name='" + name + '\'' +
                ", age=" + age +
                '}';
    }

    public void setAge(int age) {
        this.age = age;
    }

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    @MyAnnotation(name = "bayyy", age = 18)
    public void show() {
        System.out.println("Person show");
    }

    @MyAnnotation
    public void display() {
        System.out.println("Person display");
    }

    @MyAnnotation2("bayyy")
    public void test3() {
    }

    @PersonInfo(name = "bayyy", age = 25, sex = "male")
    public void test4(String name, int age, String sex) {
        System.out.println(name + "===" + age + "===" + sex);
    }

    public String getName() {
        return name;
    }


    public void setName(String name) {
        this.name = name;
    }
}
