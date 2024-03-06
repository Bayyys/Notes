package com.bayyy.config;

import com.bayyy.pojo.User;
import com.bayyy.service.UserService;
import org.apache.shiro.SecurityUtils;
import org.apache.shiro.authc.*;
import org.apache.shiro.authz.AuthorizationInfo;
import org.apache.shiro.authz.SimpleAuthorizationInfo;
import org.apache.shiro.realm.AuthorizingRealm;
import org.apache.shiro.subject.PrincipalCollection;
import org.apache.shiro.subject.Subject;
import org.springframework.beans.factory.annotation.Autowired;

// 自定义的 UserRealm
public class UserRealm extends AuthorizingRealm {
    @Autowired
    UserService userService;

    // 授权
    @Override
    protected AuthorizationInfo doGetAuthorizationInfo(PrincipalCollection principalCollection) {
        System.out.println("执行了授权 doGetAuthorizationInfo");
        SimpleAuthorizationInfo auInfo = new SimpleAuthorizationInfo();
        // 拿到当前登录的这个对象
        Subject subject = SecurityUtils.getSubject();
        User currentUser = (User) subject.getPrincipal(); // 拿到 User 对象

        // 设置当前用户的权限
        auInfo.addStringPermission(currentUser.getPerms());
        return auInfo;
    }

    // 认证
    @Override
    protected AuthenticationInfo doGetAuthenticationInfo(AuthenticationToken authenticationToken) throws AuthenticationException {
        System.out.println("执行了认证 doGetAuthenticationInfo");
        // 用户名+密码
        UsernamePasswordToken userToken = (UsernamePasswordToken) authenticationToken;
        User user = userService.queryUserByName(userToken.getUsername());
        if (user == null) {
            return null; // 抛出异常 UnknownAccountException: 用户名错误
        }
        // 返回对象为 SimpleAuthenticationInfo，参数分别为：用户名，密码，realmName
        return new SimpleAuthenticationInfo(user, user.getPwd(), "");
    }
}
