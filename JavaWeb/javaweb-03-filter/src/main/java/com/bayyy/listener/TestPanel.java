package com.bayyy.listener;

import java.awt.*;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;
import java.awt.event.WindowListener;

public class TestPanel {
    public static void main(String[] args) {
        Frame frame = new Frame("TestPanel");   // 新建一个窗体
        Panel panel = new Panel(null);  // 新建一个面板
        frame.setLayout(null);  // 设置窗体的布局

        frame.setBounds(300, 300, 500, 500);  // 设置窗体的位置和大小
        frame.setBackground(new Color(0, 0, 255));  // 设置窗体的背景颜色

        panel.setBounds(50, 50, 300, 300);  // 设置面板的位置和大小
        panel.setBackground(new Color(0, 255, 0));  // 设置面板的背景颜色

        frame.add(panel);  // 将面板添加到窗体中

        frame.setVisible(true);  // 设置窗体可见


        // 监听关闭事件
        frame.addWindowListener(new WindowListener() {

            @Override
            public void windowOpened(WindowEvent e) {
                System.out.println("窗口打开");
            }

            @Override
            public void windowClosing(WindowEvent e) {
                System.out.println("窗口关闭中ing");
                System.exit(0); // 退出程序(0:正常退出, 1:异常退出)
            }

            @Override
            public void windowClosed(WindowEvent e) {
                System.out.println("窗口已关闭");
            }

            @Override
            public void windowIconified(WindowEvent e) {
                System.out.println("窗口最小化");

            }

            @Override
            public void windowDeiconified(WindowEvent e) {
                System.out.println("窗口非最小化");

            }

            @Override
            public void windowActivated(WindowEvent e) {
                System.out.println("窗口被激活");

            }

            @Override
            public void windowDeactivated(WindowEvent e) {
                System.out.println("窗口未被激活");
            }
        });

        frame.addWindowListener(new WindowAdapter() {
            @Override
            public void windowClosing(WindowEvent e) {
                System.out.println("窗口关闭中ing");
                System.exit(0); // 退出程序(0:正常退出, 1:异常退出)
            }
        });
    }
}
