package com.bayyy.config;

import org.springframework.security.config.annotation.authentication.builders.AuthenticationManagerBuilder;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;

@EnableWebSecurity
public class SecutityConfig extends WebSecurityConfigurerAdapter {
    @Override
    protected void configure(HttpSecurity http) throws Exception {
        // 定制请求的授权规则
        // 首页所有人可以访问
        http.authorizeRequests().antMatchers("/").permitAll()
                .antMatchers("/level1/**").hasRole("vip1")
                .antMatchers("/level2/**").hasRole("vip2")
                .antMatchers("/level3/**").hasRole("vip3");

        // 开启自动配置的登录功能
        // 没有权限时会自动跳转到登录页面
        http.formLogin();
        http.logout().logoutSuccessUrl("/");    // 注销成功后来到首页
        http.csrf().disable();                  //关闭csrf功能:跨站请求伪造,默认只能通过post方式提交logout请求
        http.rememberMe().rememberMeParameter("remember");  //开启记住我功能
        http.formLogin()
                .usernameParameter("username")
                .passwordParameter("password")
                .loginPage("/toLogin")          // 自定义登录页面
                .loginProcessingUrl("/login"); // 登录表单提交请求

    }

    //定义认证规则
    @Override
    protected void configure(AuthenticationManagerBuilder auth) throws Exception {
        //在内存中定义，也可以在jdbc中去拿....
        //Spring security 5.0中新增了多种加密方式，也改变了密码的格式。
        //要想我们的项目还能够正常登陆，需要修改一下configure中的代码。我们要将前端传过来的密码进行某种方式加密
        //spring security 官方推荐的是使用bcrypt加密方式
        auth.inMemoryAuthentication().passwordEncoder(new BCryptPasswordEncoder())
                .withUser("bayyy1").password(new BCryptPasswordEncoder().encode("123456")).roles("vip1")
                .and()
                .withUser("root").password(new BCryptPasswordEncoder().encode("123456")).roles("vip1", "vip2", "vip3")
                .and()
                .withUser("bayyy2").password(new BCryptPasswordEncoder().encode("123456")).roles("vip2")
                .and()
                .withUser("bayyy3").password(new BCryptPasswordEncoder().encode("123456")).roles("vip3");
    }
}
