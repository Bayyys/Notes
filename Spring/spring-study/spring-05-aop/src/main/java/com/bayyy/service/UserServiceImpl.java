package com.bayyy.service;

public class UserServiceImpl implements UserService {
    public void add() {
        System.out.println("add a user");
    }

    public void delete() {
        System.out.println("delete a user");
    }

    public void update() {
        System.out.println("update a user");
    }

    public void select() {
        System.out.println("select a user");
    }

    public static void main(String[] args) {
        new UserServiceImpl().add();
    }
}
