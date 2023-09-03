package com.bayyy;

import redis.clients.jedis.Jedis;

public class TestPing {
    public static void main(String[] args) {
        // 1. new Jedis 对象
        Jedis jedis = new Jedis("20.24.225.117", 6379);
        jedis.auth("150bb123");
        // 2. ping
        System.out.println(jedis.ping());
    }
}
