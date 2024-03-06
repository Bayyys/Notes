package com.bayyy.mybatis_plus.service.impl;

import com.bayyy.mybatis_plus.pojo.User;
import com.bayyy.mybatis_plus.dao.UserMapper;
import com.bayyy.mybatis_plus.service.UserService;
import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import org.springframework.stereotype.Service;

/**
 * <p>
 *  服务实现类
 * </p>
 *
 * @author bayyy
 * @since 2023-08-10
 */
@Service
public class UserServiceImpl extends ServiceImpl<UserMapper, User> implements UserService {

}
