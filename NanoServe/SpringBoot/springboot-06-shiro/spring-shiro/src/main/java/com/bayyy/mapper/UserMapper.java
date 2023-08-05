package com.bayyy.mapper;

import com.bayyy.pojo.User;
import org.apache.ibatis.annotations.Mapper;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository // Repository是spring的注解，表示这是一个持久层
@Mapper // Mapper是mybatis的注解，表示这是一个mybatis的mapper类
public interface UserMapper {
    public List<User> queryUserList();

    // 根据用户名查询用户
    public User queryUserByName(String name);

    public int addUser(User user);
}
