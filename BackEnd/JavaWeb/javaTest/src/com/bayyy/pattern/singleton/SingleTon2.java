package com.bayyy.pattern.singleton;

public class SingleTon2 {
    private static SingleTon2 INSTANCE = null;

    private SingleTon2() {
    }

    //    public static synchronized SingleTon2 getInstance() {
//        if (INSTANCE==null) {
//            return new SingleTon2();
//        }
//        return INSTANCE;
//    }
    public static SingleTon2 getInstance() {
        if (INSTANCE == null) {
            synchronized (SingleTon2.class) {
                if (INSTANCE == null) {
                    return new SingleTon2();
                }
            }
        }
        return INSTANCE;
    }
}
