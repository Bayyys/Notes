package com.bayyy.dao;

import com.bayyy.pojo.User;
import com.bayyy.utils.MyBatisUtils;
import org.apache.ibatis.session.SqlSession;
import org.junit.Test;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class UserMapperTest {
    @Test
    public void testSelectAll() {
        // try-with-resources: try内部的资源会自动释放(且是先声明的资源先释放)
        try (SqlSession sqlSession = MyBatisUtils.getSqlSession()) {
            sqlSession.getMapper(UserMapper.class).getUserList().forEach(System.out::println);
        }
//        // 1. 获取sqlSession对象
//        SqlSession sqlSession = MyBatisUtils.getSqlSession();
//        // 2. 执行sql
//        // 方式一：getMapper
//        UserMapper userMapper = sqlSession.getMapper(UserMapper.class);
//        List<User> userList = userMapper.getUserList();
//        for (User user : userList) {
//            System.out.println(user);
//        }
//
//        // 方式二：不推荐
//        List<User> userList2 = sqlSession.selectList("com.bayyy.dao.UserMapper.getUserList");
//        for (User user : userList2) {
//            System.out.println(user);
//        }
//
//        // 3. 关闭sqlSession
//        sqlSession.close();
    }

    @Test
    public void testSelectById() {
        try (SqlSession sqlSession = MyBatisUtils.getSqlSession()) {
            UserMapper mapper = sqlSession.getMapper(UserMapper.class);
            User user = mapper.getUserById(1);
            System.out.println(user);
        }
    }

    @Test
    public void testAdd() {
        try (SqlSession sqlSession = MyBatisUtils.getSqlSession()) {
            int add = sqlSession.getMapper(UserMapper.class).addUser(new User(4, "长江四号", "123456"));
            if (add > 0) {
                User user = sqlSession.getMapper(UserMapper.class).getUserById(4);
                System.out.println(user);
            } else {
                System.out.println("插入失败");
            }
            sqlSession.commit();
        }
    }

    @Test
    public void testDelete() {
        try (SqlSession sqlSession = MyBatisUtils.getSqlSession()) {
            int delete = sqlSession.getMapper(UserMapper.class).deleteUser(4);
            if (delete > 0) {
                System.out.println("删除成功");
                sqlSession.getMapper(UserMapper.class).getUserList().forEach(System.out::println);
            } else {
                System.out.println("删除失败");
            }
            sqlSession.commit();
        }
    }

    @Test
    public void testUpdate() {
        try (SqlSession sqlSession = MyBatisUtils.getSqlSession()) {
            UserMapper mapper = sqlSession.getMapper(UserMapper.class);
            int update = mapper.updateUser(new User(4, "长江四号", "654321"));
            if (update > 0) {
                System.out.println("修改成功");
                User user = mapper.getUserById(4);
                System.out.println(user);
            } else {
                System.out.println("修改失败");
            }
            sqlSession.commit();
        }
    }

    @Test
    public void testMapUpdate() {
        try (SqlSession sqlSession = MyBatisUtils.getSqlSession()) {
            Map<String, Object> map = new HashMap<String, Object>();
            map.put("mapId", 4);
            map.put("mapName", "黄河四号");
            System.out.println(sqlSession.getMapper(UserMapper.class).mapUpdate(map));
            sqlSession.commit();
        }
    }
}
