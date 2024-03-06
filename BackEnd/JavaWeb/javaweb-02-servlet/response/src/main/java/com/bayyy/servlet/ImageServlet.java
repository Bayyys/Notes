package com.bayyy.servlet;

import javax.imageio.ImageIO;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.IOException;
import java.util.Random;

public class ImageServlet extends HttpServlet {
    // 生成随机数
    private String makeNum(){
        Random random = new Random();
        String num = random.nextInt(99999999) + "";
        StringBuffer sb = new StringBuffer();
        for (int i = 0; i < 8 - num.length(); i++) {
            sb.append("0");
        }
        String verify = sb.toString() + num;
        return verify;
    }

    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        System.out.println("进入了ImageServlet");
        // 如何让浏览器5秒刷新一次
        resp.setHeader("refresh", "5");    // 设置refresh响应头，让浏览器每隔5秒刷新一次

        // 在内存中创建一个图片
        BufferedImage image = new BufferedImage(80, 20, BufferedImage.TYPE_INT_RGB);    // 80*20的图片，TYPE_INT_RGB是颜色
        // 得到图片
        Graphics pen = image.getGraphics();   // 笔
        // 设置图片的背景颜色
        pen.setColor(Color.white);
        pen.fillRect(0, 0, 80, 20);    // 填充矩形，从(0,0)开始，宽80，高20
        // 给图片写数据
        pen.setColor(Color.blue);
        pen.setFont(new Font(null, Font.BOLD, 20));    // 设置字体: 字体、字体样式、字体大小
        pen.drawString(makeNum(), 0, 20);    // 从(0,20)开始写
        // 告诉浏览器，这个请求用图片的方式打开
        resp.setContentType("image/jpeg");    // 响应头，告诉浏览器，这个请求用图片的方式打开
        // 网站存在缓存，不让浏览器缓存
        resp.setDateHeader("expires", -1);
        resp.setHeader("Cache-Control", "no-cache");    // 不缓存
        resp.setHeader("Pragma", "no-cache");    // 不缓存
        // 把图片写给浏览器
        ImageIO.write(image, "jpg", resp.getOutputStream());
    }

    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        doGet(req, resp);
    }
}
