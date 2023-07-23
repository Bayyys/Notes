package com.bayyy.controller;

import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONObject;
import com.bayyy.pojo.User;
import com.bayyy.utils.JsonUtils;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.SerializationFeature;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;

import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;

@RestController // 代表这个类的所有方法返回的数据直接写给浏览器，如果是对象转为json数据
public class UserController {
    @RequestMapping("/j1")
//    @ResponseBody // 不会走视图解析器，会直接返回一个字符串
    public String json1() throws JsonProcessingException {
        // jackson, ObjectMapper
        ObjectMapper objectMapper = new ObjectMapper();
        // 创建一个对象
        User user = new User("Bayyy", 18, "男");
        String s = objectMapper.writeValueAsString(user);
        return s;
    }

    @RequestMapping("/j2")
    public String json2() throws JsonProcessingException {
        ObjectMapper mapper = new ObjectMapper();
        List<User> userList = new ArrayList<User>();
        User user1 = new User("Bayyy1", 18, "男");
        User user2 = new User("Bayyy2", 18, "男");
        User user3 = new User("Bayyy3", 18, "男");
        User user4 = new User("Bayyy4", 18, "男");
        userList.add(user1);
        userList.add(user2);
        userList.add(user3);
        userList.add(user4);
        String s = mapper.writeValueAsString(userList);
        return s;
    }

    @RequestMapping("/j3")
    public String json3() throws JsonProcessingException {
        ObjectMapper mapper = new ObjectMapper();
        mapper.configure(SerializationFeature.WRITE_DATES_AS_TIMESTAMPS, false);
        SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
        mapper.setDateFormat(sdf);
        Date date = new Date();
        return mapper.writeValueAsString(date);
    }

    @RequestMapping("/j4")
    public String json4() throws JsonProcessingException {
        Date date = new Date();
        String json = JsonUtils.getJson(date);
        // String json = JsonUtils.getJson(date, "yyyy-MM-dd HH:mm:ss");
        return json;
    }

    @RequestMapping("/j5")
    public String json5() throws JsonProcessingException {
        ObjectMapper mapper = new ObjectMapper();
        List<User> userList = new ArrayList<User>();
        User user1 = new User("Bayyy1", 18, "男");
        User user2 = new User("Bayyy2", 18, "男");
        User user3 = new User("Bayyy3", 18, "男");
        User user4 = new User("Bayyy4", 18, "男");
        userList.add(user1);
        userList.add(user2);
        userList.add(user3);
        userList.add(user4);
        String s = JSON.toJSONString(userList);
        System.out.println("*******Java对象 转 JSON字符串*******");
        String str1 = JSON.toJSONString(userList);
        System.out.println("JSON.toJSONString(list)==>"+str1);
        String str2 = JSON.toJSONString(user1);
        System.out.println("JSON.toJSONString(user1)==>"+str2);

        System.out.println("\n****** JSON字符串 转 Java对象*******");
        User jp_user1=JSON.parseObject(str2,User.class);
        System.out.println("JSON.parseObject(str2,User.class)==>"+jp_user1);

        System.out.println("\n****** Java对象 转 JSON对象 ******");
        JSONObject jsonObject1 = (JSONObject) JSON.toJSON(user2);
        System.out.println("(JSONObject) JSON.toJSON(user2)==>"+jsonObject1.getString("name"));

        System.out.println("\n****** JSON对象 转 Java对象 ******");
        User to_java_user = JSON.toJavaObject(jsonObject1, User.class);
        System.out.println("JSON.toJavaObject(jsonObject1, User.class)==>"+to_java_user);
        return s;
    }
}
