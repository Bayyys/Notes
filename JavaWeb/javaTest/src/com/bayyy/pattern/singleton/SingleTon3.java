package com.bayyy.pattern.singleton;

public class SingleTon3 {
    private SingleTon3() {}
    private static class SingleTon3Holder {
        static SingleTon3 INSTANCE = new SingleTon3();
    }
    public static SingleTon3 getInstance() {
        return SingleTon3Holder.INSTANCE;
    }
}
