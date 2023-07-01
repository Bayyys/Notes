package src.sql;

import src.sql.utils.JDBCUtils;

import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class TestUtil {
    public static void main(String[] args) {
        Connection connection = null;
        Statement statement = null;
        ResultSet rs = null;
        try {
            connection = JDBCUtils.getConnection(); // 获取数据库连接
            statement = connection.createStatement();   // 获取执行SQL的对象
            String sql = "SELECT * FROM users"; // 要执行的SQL
            rs = statement.executeQuery(sql);  // 执行SQL, 返回结果集
            while (rs.next()) {
                System.out.println("id=" + rs.getObject("id"));
                System.out.println("name=" + rs.getObject("name"));
                System.out.println("password=" + rs.getObject("password"));
                System.out.println("email=" + rs.getObject("email"));
                System.out.println("birthday=" + rs.getObject("birthday"));
            }
            sql = "INSERT INTO users(id, `NAME`, `PASSWORD`, `email`, `birthday`) VALUES(5, 'test', '123456', '123@qq.com', '1979-12-04')";
            int count = statement.executeUpdate(sql); // 执行SQL, 返回影响的行数
            if (count > 0) {
                System.out.println("添加成功");
            } else {
                System.out.println("添加失败");
            }
        } catch (SQLException e) {
            throw new RuntimeException(e);
        } finally {
            JDBCUtils.release(connection, statement, rs);
        }


    }
}
