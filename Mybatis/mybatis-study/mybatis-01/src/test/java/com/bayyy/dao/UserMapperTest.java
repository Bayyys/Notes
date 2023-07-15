package com.bayyy.dao;

import com.bayyy.pojo.User;
import com.bayyy.utils.MyBatisUtils;
import org.apache.ibatis.session.SqlSession;
import org.junit.Test;

import java.util.List;

public class UserMapperTest {
    @Test
    public void test() {
        // try-with-resources: try内部的资源会自动释放(且是先声明的资源先释放)
        try (SqlSession sqlSession = MyBatisUtils.getSqlSession()) {
            UserMapper userMapper = sqlSession.getMapper(UserMapper.class);
            List<User> userList = userMapper.getUserList();
            for (User user : userList) {
                System.out.println(user);
            }
        } catch (Exception e) {
            e.printStackTrace();
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
}
