package com.bayyy;

import com.bayyy.pojo.User;
import com.bayyy.utils.RedisUtil;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.data.redis.core.RedisTemplate;

@SpringBootTest
class Redis02SpringbootApplicationTests {

    @Autowired
    @Qualifier("redisTemplate")     // 与 redisConfig.java 中的 @Bean("redisTemplate") 对应
    private RedisTemplate redisTemplate;

    @Autowired
    private RedisUtil redisUtil;

    @Test
    void contextLoads() {
        redisTemplate.opsForValue().set("name", "白澳阳");
        System.out.println("name: " + redisTemplate.opsForValue().get("name"));
    }


    @Test
    public void testSerializable() throws JsonProcessingException {
        User user = new User("白澳阳", 18);
        String jsonUser = new ObjectMapper().writeValueAsString(user);
        redisTemplate.opsForValue().set("user", user);
        System.out.println("user: " + redisTemplate.opsForValue().get("user"));
    }

    @Test
    public void testUtils() {
        redisUtil.set("name", "白澳阳");
        redisUtil.set("age", 18);
        System.out.println(redisUtil.hasKey("name"));
        System.out.println(redisUtil.get("name"));
        redisUtil.del("name", "age");
    }
}
