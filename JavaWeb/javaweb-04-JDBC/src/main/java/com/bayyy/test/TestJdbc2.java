package com.bayyy.test;

import org.junit.jupiter.api.Test;

import java.sql.*;

public class TestJdbc2 {
    public static void main(String[] args) throws ClassNotFoundException, SQLException {
        // 加载驱动
        Class.forName("com.mysql.cj.jdbc.Driver");

        // 配置信息
        String url = "jdbc:mysql://localhost:3306/jdbc?useUnicode=true&characterEncoding=utf8&useSSL=false&serverTimezone=GMT%2B8";
        String name = "root";
        String pwd = "123456";

        // 建立连接, 返回连接对象 Connection
        Connection connection = DriverManager.getConnection(url, name, pwd);

        // 预编译sql语句
        String sql = "SELECT * FROM users WHERE id = ?";
        PreparedStatement preparedStatement = connection.prepareStatement(sql);
        preparedStatement.setInt(1, 1);

        ResultSet resultSet = preparedStatement.executeQuery();

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
        preparedStatement.close();
        connection.close();
    }

    @Test
    public void test() {
        System.out.println("test");
        System.out.println(5 / 0);
    }
}
