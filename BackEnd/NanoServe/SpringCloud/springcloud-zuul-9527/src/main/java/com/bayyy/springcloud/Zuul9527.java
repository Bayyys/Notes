package com.bayyy.springcloud;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.client.discovery.EnableDiscoveryClient;
import org.springframework.cloud.netflix.hystrix.EnableHystrix;
import org.springframework.cloud.netflix.zuul.EnableZuulProxy;
import org.springframework.cloud.openfeign.EnableFeignClients;
import org.springframework.cloud.openfeign.FeignClient;

@SpringBootApplication
@EnableZuulProxy // 开启Zuul的功能
@EnableDiscoveryClient
@EnableHystrix
@EnableFeignClients
public class Zuul9527 {
    public static void main(String[] args) {
        SpringApplication.run(Zuul9527.class, args);
    }
}
