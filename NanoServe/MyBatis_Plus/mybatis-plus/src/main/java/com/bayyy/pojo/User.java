package com.bayyy.pojo;

import com.baomidou.mybatisplus.annotation.*;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.time.LocalDateTime;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class User {
    @TableId(type = IdType.AUTO)
    private int id;
    private String name;
    private int age;
    private String email;
    // 乐观锁
    @Version
    private int version;
    // 字段添加填充内容
    // INSERT：插入时填充
    @TableField(fill = FieldFill.INSERT)
    private LocalDateTime createTime;
    // UPDATE：更新时填充
    @TableField(fill = FieldFill.INSERT_UPDATE)
    private LocalDateTime updateTime;
}
