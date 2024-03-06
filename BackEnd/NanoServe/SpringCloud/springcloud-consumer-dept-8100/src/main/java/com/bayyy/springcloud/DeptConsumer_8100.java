package com.bayyy.springcloud;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.client.discovery.EnableDiscoveryClient;
import org.springframework.cloud.loadbalancer.annotation.LoadBalancerClient;
import org.springframework.cloud.loadbalancer.core.RandomLoadBalancer;

@SpringBootApplication
@EnableDiscoveryClient
public class DeptConsumer_8100 {
    public static void main(String[] args) {
        SpringApplication.run(DeptConsumer_8100.class, args);
    }
}
