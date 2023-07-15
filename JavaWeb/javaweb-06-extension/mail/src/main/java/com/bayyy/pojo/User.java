package com.bayyy.pojo;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data   // 生成get set方法
@AllArgsConstructor // 生成全参构造器
@NoArgsConstructor  // 生成无参构造器
public class User {
    private String username;
    private String password;
    private String email;
}
