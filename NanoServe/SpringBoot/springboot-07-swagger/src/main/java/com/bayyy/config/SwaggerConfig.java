package com.bayyy.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.core.env.Environment;
import org.springframework.core.env.Profiles;
import springfox.documentation.RequestHandler;
import springfox.documentation.builders.PathSelectors;
import springfox.documentation.builders.RequestHandlerSelectors;
import springfox.documentation.service.ApiInfo;
import springfox.documentation.service.Contact;
import springfox.documentation.spi.DocumentationType;
import springfox.documentation.spring.web.plugins.Docket;

import java.util.ArrayList;
import java.util.function.Predicate;

import static springfox.documentation.service.ApiInfo.DEFAULT_CONTACT;

@Configuration
public class SwaggerConfig {
    // 配置Swagger2的Docket的bean实例
    @Bean
    public Docket docket(Environment environment) {
        // 设置要显示的Swagger环境
        Profiles profiles = Profiles.of("dev", "test");
        // 判断当前是否处于该环境
        boolean flag = environment.acceptsProfiles(profiles);
        return new Docket(DocumentationType.SWAGGER_2)
                .apiInfo(apiInfo())
                .groupName("group1")    // 配置分组
                .enable(flag) // 是否启用Swagger
                .select()   // 配置扫描接口
                // RequestHandlerSelectors配置要扫描接口的方式
                // basePackage指定要扫描的包
                /**
                 * any() 扫描全部
                 * none() 不扫描
                 * withClassAnnotation() 扫描类上的注解，参数是一个注解的反射对象
                 * withMethodAnnotation() 扫描方法上的注解
                 * basePackage() 扫描指定包
                 */
                .apis(RequestHandlerSelectors.basePackage("com.bayyy.controller"))  // basePackage() 扫描指定包
                // paths() 过滤什么路径
                // PathSelectors.ant() 过滤指定路径
                /**
                 * ant() 过滤指定路径
                 * any() 过滤全部
                 * none() 不过滤
                 * regex() 正则表达式
                 */
                .paths(PathSelectors.ant("/test/**"))
                .build();   // build() 创建Docket实例
    }

    @Bean
    public Docket docket2() {
        return new Docket(DocumentationType.SWAGGER_2)
                .groupName("group2");
    }

    @Bean
    public Docket docket3() {
        return new Docket(DocumentationType.SWAGGER_2)
                .groupName("group3");
    }
    @Bean
    public Docket docket4() {
        return new Docket(DocumentationType.SWAGGER_2)
                .groupName("group4");
    }
    // 配置Swagger的apiInfo
    private ApiInfo apiInfo() {
        // 源码中有默认的apiInfo，可以不用配置
        /**
         return new ApiInfo(
         "Api Documentation",
         "Api Documentation",
         "1.0",
         "urn:tos",
         DEFAULT_CONTACT,
         "Apache 2.0",
         "http://www.apache.org/licenses/LICENSE-2.0",
         new ArrayList<>());
         */
        Contact contact = new Contact("bayyy", "http://www.bayyy.com", "bayyy@bayyy");
        return new ApiInfo(
                "Bayyy Swagger",
                "Bayyy Swagger Api Documentation",
                "1.1-beta",
                "http://www.bayyy.com",
                contact,
                "Apache 2.0",
                "http://www.apache.org/licenses/LICENSE-2.0",
                new ArrayList<>());
    }
}
