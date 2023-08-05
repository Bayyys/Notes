package com.bayyy.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import springfox.documentation.service.ApiInfo;
import springfox.documentation.service.Contact;
import springfox.documentation.spi.DocumentationType;
import springfox.documentation.spring.web.plugins.Docket;

import java.util.ArrayList;

import static springfox.documentation.service.ApiInfo.DEFAULT_CONTACT;

@Configuration
public class SwaggerConfig {
    // 配置Swagger2的Docket的bean实例
    @Bean
    public Docket docket() {
        return new Docket(DocumentationType.SWAGGER_2)
                .apiInfo(apiInfo());
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
