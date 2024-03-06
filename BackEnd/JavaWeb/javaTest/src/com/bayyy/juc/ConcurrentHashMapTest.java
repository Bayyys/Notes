package com.bayyy.juc;

import javax.swing.text.html.parser.Entity;
import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;

public class ConcurrentHashMapTest {
    public static void main(String[] args) {
        // 1. 创建集合对象
        // 实现类：ConcurrentHashMap
        ConcurrentHashMap<String, String> map = new ConcurrentHashMap<String, String>();
        // 2. 添加元素
        map.put("hello", "world");
        map.put("java", "bayyy");
        map.put("hello", "bayyy");  // key相同，value覆盖
        // 3. 遍历集合
        for (Map.Entry<String, String> entity : map.entrySet()) {
            System.out.println(entity.getKey() + "=" + entity.getValue());
        }
    }
}
