package com.bayyy.config;

import at.pollux.thymeleaf.shiro.dialect.ShiroDialect;
import org.apache.shiro.spring.web.ShiroFilterFactoryBean;
import org.apache.shiro.web.mgt.DefaultWebSecurityManager;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import java.util.LinkedHashMap;
import java.util.Map;

@Configuration
public class ShiroConfig {
    // 整合 ShiroDialect：用来整合 Shiro 和 thymeleaf
    @Bean(name = "shiroDialect")
    public ShiroDialect getShiroDialect() {
        return new ShiroDialect();
    }


    // ShiroFilterFactoryBean
    @Bean(name = "shiroFilterFactoryBean")
    public ShiroFilterFactoryBean getShiroFilterFactoryBean(@Qualifier("getDefaultWebSecurityManager") DefaultWebSecurityManager getDefaultWebSecurityManager) {
        ShiroFilterFactoryBean bean = new ShiroFilterFactoryBean();
        // 设置安全管理器
        bean.setSecurityManager(getDefaultWebSecurityManager);


        /**
         * anon: 无需认证就可以访问
         * authc: 必须认证了才能访问
         * user: 必须拥有 记住我 功能才能用
         * perms: 拥有对某个资源的权限才能访问
         * role: 拥有某个角色权限才能访问
         */
        Map<String, String> filterMap = new LinkedHashMap<>();
        // 授权，正常情况下，没有授权会跳转到未授权页面
//        filterMap.put("/user/add", "authc");
//        filterMap.put("/user/update", "authc");

        // 授权
        filterMap.put("/user/add", "perms[user:add]");
        filterMap.put("/user/update", "perms[user:update]");

        // 通配符进行设置拦截
        filterMap.put("/user/*", "authc");
        bean.setFilterChainDefinitionMap(filterMap);

        // 设置登录的请求
        bean.setLoginUrl("/toLogin");

        // 设置未授权的请求
        bean.setUnauthorizedUrl("/unauthorized");
        return bean;
    }

    // DefaultWebSecurityManager
    @Bean(name = "getDefaultWebSecurityManager")
    public DefaultWebSecurityManager getDefaultWebSecurityManager(@Qualifier("userRealm") UserRealm userRealm) {
        DefaultWebSecurityManager securityManager = new DefaultWebSecurityManager();
        // 关联 UserRealm
        securityManager.setRealm(userRealm);
        return securityManager;
    }

    // 创建 realm 对象，需要自定义类
    @Bean(name = "userRealm")
    public UserRealm userRealm() {
        return new UserRealm();
    }
}
