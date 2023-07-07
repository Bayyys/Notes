package com.bayyy.test;

import java.sql.*;

public class TestJdbc {
    public static void main(String[] args) throws ClassNotFoundException, SQLException {
        // 加载驱动
        Class.forName("com.mysql.cj.jdbc.Driver");

        // 配置信息
        String url = "jdbc:mysql://localhost:3306/jdbc?useUnicode=true&characterEncoding=utf8&useSSL=false&serverTimezone=GMT%2B8";
        String name = "root";
        String password = "123456";

        // 建立连接, 返回连接对象 Connection
        Connection connection = DriverManager.getConnection(url, name, password);

        // 创建数据库操作对象 Statement
        Statement statement = connection.createStatement();

        // 执行sql语句
        String sql = "SELECT * FROM users";

        // 返回结果集
        ResultSet resultSet = statement.executeQuery(sql);

        // 处理结果集
        while (resultSet.next()) {
            System.out.println("id=" + resultSet.getObject("id"));
            System.out.println("name=" + resultSet.getObject("name"));
            System.out.println("password=" + resultSet.getObject("password"));
            System.out.println("email=" + resultSet.getObject("email"));
            System.out.println("birthday=" + resultSet.getObject("birthday"));
        }

        // 关闭连接
        resultSet.close();
        statement.close();
        connection.close();
    }
}
