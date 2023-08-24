package com.bayyy.springcloud.config;

import org.springframework.cloud.client.loadbalancer.LoadBalanced;
import org.springframework.cloud.loadbalancer.annotation.LoadBalancerClient;
import org.springframework.cloud.loadbalancer.annotation.LoadBalancerClients;
import org.springframework.cloud.loadbalancer.core.RandomLoadBalancer;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.client.RestTemplate;

@Configuration
public class ConfigBean {
    @Bean
    @LoadBalanced   // 配置负载均衡实现
    // 使用 RestTemplate 访问 restful
    public RestTemplate getRestTemplate() {
        return new RestTemplate();
    }

    /**
     * 负载均衡算法-IRule：
     * 1. RoundRobinLoadBalancer 轮询
     * 2. RandomLoadBalancer 随机
     */
}
