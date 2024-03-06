package com.bayyy.dao;

import com.baomidou.mybatisplus.core.mapper.BaseMapper;
import com.bayyy.pojo.User;
import org.apache.ibatis.annotations.Mapper;
import org.springframework.stereotype.Repository;

// 在对应的Mapper上面继承基本的类 BaseMapper
@Mapper
public interface UserMapper extends BaseMapper<User> {
    // 此时，所有的CRUD操作都已经编写完成
}
