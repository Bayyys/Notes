package src.sql;

import java.sql.*;

// 第一个JDBC程序
public class JDBCDemo1 {
    public static void main(String[] args) throws ClassNotFoundException, SQLException {
        // 1. 加载驱动
        Class.forName("com.mysql.jdbc.Driver");

        // 2. 用户信息和url
        String url = "jdbc:mysql://localhost:3306/jdbc?useUnicode=true&characterEncoding=utf8&&useSSL=false";   // useUnicode: 使用Unicode字符集 characterEncoding: 指定字符编码   useSSL: 是否使用安全套接字
        String name = "root";
        String password = "123456";

        // 3. 创建连接, 返回数据库对象, Connection代表数据库
        Connection connection = DriverManager.getConnection(url, name, password);

        // 4. 执行SQL语句的对象, Statement代表要执行的SQL的对象
        Statement statement = connection.createStatement();

        // 5. 执行SQL语句, 返回结果集
        String sql = "SELECT * FROM users";
        ResultSet resultSet = statement.executeQuery(sql);  // executeQuery: 执行查询操作, 返回ResultSet对象, 其中封装了全部的查询结果

        // 6. 遍历查询结果
        while (resultSet.next()) {
            System.out.println("id=" + resultSet.getObject("id"));
            System.out.println("name=" + resultSet.getObject("name"));
            System.out.println("password=" + resultSet.getObject("password"));
            System.out.println("email=" + resultSet.getObject("email"));
            System.out.println("birthday=" + resultSet.getObject("birthday"));
        }

        // 7. 释放连接
        resultSet.close();
        statement.close();
        connection.close();
    }
}
