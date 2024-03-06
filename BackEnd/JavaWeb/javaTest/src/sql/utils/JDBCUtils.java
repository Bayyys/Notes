package src.sql.utils;

import java.io.IOException;
import java.io.InputStream;
import java.sql.*;
import java.util.Properties;

public class JDBCUtils {
    private static String driver = "";
    private static String url = "";
    private static String usename = "";
    private static String password = "";


    static {
        try {
            InputStream in = JDBCUtils.class.getClassLoader().getResourceAsStream("src/db.properties");
            Properties properties = new Properties();
            properties.load(in);

            driver = properties.getProperty("driver");
            url = properties.getProperty("url");
            usename = properties.getProperty("username");
            password = properties.getProperty("password");

            Class.forName(driver);

        } catch (IOException | ClassNotFoundException e) {
            throw new RuntimeException(e);
        }


    }

    // 获取连接
    public static Connection getConnection() throws SQLException {
        return DriverManager.getConnection(url, usename, password);
    }

    // 释放连接
    public static void release(Connection connection, Statement statement, ResultSet resultSet) {
        try {
            resultSet.close();
        } catch (SQLException e) {
            throw new RuntimeException(e);
        } catch (Exception e) {

        }

        try {
            statement.close();
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }

        try {
            connection.close();
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
    }
}
