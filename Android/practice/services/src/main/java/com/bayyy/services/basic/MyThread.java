package com.bayyy.services.basic;

public class MyThread {
  public static void main(String[] args) {
    // Thread
    UseThread useThread = new UseThread();
    useThread.start();

    // Runnable
    new Thread(new UseRunnable()).start();

    // 匿名类
    new Thread(() -> {
      // 实现逻辑
    }).start();
  }

  static class UseThread extends Thread {
    @Override
    public void run() {
      super.run();
      // 实现逻辑
    }
  }

  static class UseRunnable implements Runnable {
    @Override
    public void run() {
      // 实现逻辑
    }
  }
}
