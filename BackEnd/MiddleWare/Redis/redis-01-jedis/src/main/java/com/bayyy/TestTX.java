package com.bayyy;

import org.json.JSONObject;
import redis.clients.jedis.Jedis;
import redis.clients.jedis.Transaction;

public class TestTX {
    public static void main(String[] args) {
        Jedis jedis = new Jedis("20.24.225.117", 6379);
        jedis.auth("150bb123");

        JSONObject json = new JSONObject();
        json.put("hello", "world");
        json.put("name", "bayyy");
        json.put("age", "18");

        // 开启事务
        Transaction multi = jedis.multi();
        String string = json.toString();
        try {
            multi.set("user1", string);
            multi.set("user2", string);
            // 执行事务
            multi.exec();
        } catch (Exception e) {
            multi.discard();
            e.printStackTrace();
        } finally {
            System.out.println(jedis.get("user1"));
            System.out.println(jedis.get("user2"));
            jedis.close();
        }
    }
}
