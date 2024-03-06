package com.bayyy.dao;

import com.bayyy.pojo.User;
import org.apache.ibatis.annotations.*;

import java.util.HashMap;
import java.util.List;

public interface UserMapper {
    // 查询全部用户
    @Select("select * from user")
    List<User> getUserList();

    // 根据id查询用户
    // @Param("id") 与 #{id} 对应
    // 如果存在多个参数，必须需要使用 @Param
    @Select("select * from user where id = #{id}")
    User getUserById(@Param("id") int id);

    // 插入一个用户
    // 引用对象的属性名可以直接使用 #{属性名}
    @Insert("insert into user(id, name, pwd) values(#{id}, #{name}, #{pwd})")
    int addUser(User user);

    // 修改一个用户
    @Update("update user set name = #{name} where id = #{id}")
    int updateUser(User user);

    // 删除一个用户
    @Delete("delete from user where id = #{id}")
    int deleteUser(int id);
}
