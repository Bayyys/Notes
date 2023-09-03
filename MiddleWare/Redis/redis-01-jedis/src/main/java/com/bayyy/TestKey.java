package com.bayyy;

import redis.clients.jedis.Jedis;

public class TestKey {
    public static void main(String[] args) {
        Jedis jedis = new Jedis("20.24.225.117", 6379);
        jedis.auth("150bb123");

        System.out.println("清空数据：" + jedis.flushDB());
        System.out.println("判断某个键是否存在：" + jedis.exists("name"));
        System.out.println("新增<'name','bay'>的键值对：" + jedis.set("name", "bay"));
        System.out.println("新增<'age','18'>的键值对：" + jedis.set("age", "18"));
        System.out.println("系统中所有的键如下：");
        System.out.println(jedis.keys("*"));
        System.out.println("删除键age：" + jedis.del("age"));
        System.out.println("判断键age是否存在：" + jedis.exists("age"));
        System.out.println("查看键name所存储的值的类型：" + jedis.type("name"));
        System.out.println("随机返回key空间的一个：" + jedis.randomKey());
        System.out.println("重命名key：" + jedis.rename("name", "nameNew"));
        System.out.println("取出改后的name：" + jedis.get("nameNew"));
        System.out.println("按索引查询：" + jedis.select(0));
        System.out.println("删除当前选择数据库中的所有key：" + jedis.flushDB());
        System.out.println("返回当前数据库中key的数目：" + jedis.dbSize());
        System.out.println("删除所有数据库中的所有key：" + jedis.flushAll());
    }
}
