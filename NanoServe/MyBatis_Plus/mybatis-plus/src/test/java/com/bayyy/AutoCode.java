package com.bayyy;

import com.baomidou.mybatisplus.annotation.FieldFill;
import com.baomidou.mybatisplus.annotation.IdType;
import com.baomidou.mybatisplus.generator.AutoGenerator;
import com.baomidou.mybatisplus.generator.FastAutoGenerator;
import com.baomidou.mybatisplus.generator.IFill;
import com.baomidou.mybatisplus.generator.config.*;
import com.baomidou.mybatisplus.generator.config.builder.ConfigBuilder;
import com.baomidou.mybatisplus.generator.config.rules.DateType;
import com.baomidou.mybatisplus.generator.config.rules.NamingStrategy;
import com.baomidou.mybatisplus.generator.engine.FreemarkerTemplateEngine;
import com.baomidou.mybatisplus.generator.fill.Column;

import java.util.ArrayList;
import java.util.List;

public class AutoCode {
    public static void main(String[] args) {
        FastAutoGenerator.create("jdbc:mysql://localhost:3306/mybatis_plus?useUnicode=true&characterEncoding=utf-8&useSSL=false&serverTimezone=UTC", "root", "123456")
                .globalConfig(builder -> {  // 全局配置
                    builder.author("bayyy") // 作者
                            .disableOpenDir()   // 禁用打开输出目录
                            .outputDir(System.getProperty("user.dir") + "/src/main/java")   // 输出目录
                            .enableSwagger()    // 开启swagger模式
                            .dateType(DateType.ONLY_DATE)   // 时间类型
                            .commentDate("yyyy-MM-dd"); // 注释日期格式
                })
                .packageConfig(builder -> { // 包配置
                    builder.parent("com.bayyy")    // 父包名
                            .moduleName("mybatis_plus")    // 父包模块名
                            .entity("pojo") // 实体类包名
                            .service("service") // service包名
                            .serviceImpl("service.impl")   // serviceImpl包名
                            .mapper("dao")  // mapper包名
                            .xml("dao.mapper")  // mapper XML包名
                            .controller("controller")   // controller包名
                            .pathInfo(null); // 路径配置信息
                })
                .strategyConfig(builder -> {    // 策略配置
                    builder.addInclude("user")  // 指定生成的表名(默认null)
                            .addTablePrefix("t_")   // 表名前缀(默认null, 如果指定了表名前缀, 生成的实体类名将会去除前缀)
                            .addFieldSuffix("_flag")   // 字段名后缀(默认null, 如果指定了字段名后缀, 生成的实体类字段名将会去除后缀)
                            .enableCapitalMode()    // 开启全局大写命名(默认false, 例如: 表名 user -> 实体类名 User)
                            /* 实体类配置 */
                            .entityBuilder()    // 实体类配置
                            .enableLombok() // 开启lombok(默认false)
                            .columnNaming(NamingStrategy.underline_to_camel)    // 字段命名策略(默认underline_to_camel:下划线转驼峰命名)
                            .naming(NamingStrategy.underline_to_camel) // 实体命名策略(默认underline_to_camel:下划线转驼峰命名)
                            .addTableFills(new Column("update_time", FieldFill.INSERT))    // 表字段填充(默认null)
                            .addTableFills(new Column("create_time", FieldFill.INSERT_UPDATE))   // 表字段填充(默认null)
                            .versionColumnName("version")   // 乐观锁字段名(默认null)
                            .idType(IdType.AUTO)   // 主键类型(默认null, 改为IdType.AUTO即可使用自增主键)
                            .logicDeleteColumnName("deleted")   // 逻辑删除字段名(默认null)
                            /* Service 配置 */
                            .serviceBuilder()   // service配置
                            .enableFileOverride()   // 开启文件覆盖(默认false)
                            .formatServiceImplFileName("%sServiceImpl") // service实现类命名格式(默认null)
                            .formatServiceFileName("%sService") // service接口命名格式(默认null)
                            /* Controller 配置 */
                            .controllerBuilder()
                            .enableRestStyle()  // 开启restController(默认false)
                            .enableHyphenStyle()    // 开启驼峰转连字符(默认false, 例如: 表名 user, 字段名 id -> localhost:8080/user_id_1)
                            .build();
                })
                .execute();

    }
}
