package com.bayyy.springcloud.pojo;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.experimental.Accessors;

import java.io.Serializable;

@Data
@NoArgsConstructor
@Accessors(chain=true)  // 链式写法(Dept dept = new Dept(); dept.setDeptNo(11).setDname("RD").setDbSource("DB01");)
public class Dept implements Serializable {
    private Long deptId;    // 部门编号(bigint-Long)
    private String dname;   // 部门名称
    private String dbSource;   // 来自哪个数据库，因为微服务架构可以一个服务对应一个数据库，同一个信息被存储到不同数据库

    public Dept(String dname) {
        this.dname = dname;
    }
}
