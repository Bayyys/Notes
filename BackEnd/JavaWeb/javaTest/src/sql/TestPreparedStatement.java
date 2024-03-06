package src.sql;

import src.sql.utils.JDBCUtils;

import java.sql.Connection;
import java.util.Date;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class TestPreparedStatement {
    public static void main(String[] args) {
        Connection con = null;
        PreparedStatement pst = null;

        try {
            con = JDBCUtils.getConnection();
            // 预编译SQL, 先写SQL, 然后不执行
            // 区别：
            // 使用？占位符代替参数
            String sql = "INSERT INTO users(id, `NAME`, `PASSWORD`, `email`, `birthday`) VALUES(?, ?, ?, ?, ?)";
            pst = con.prepareStatement(sql);    // 获取执行SQL的对象, 预编译SQL语句

            // 手动给参数赋值
            pst.setInt(1, 6);
            pst.setString(2, "test");
            pst.setString(3, "123456");
            pst.setString(4, "123321@qq.com");
            pst.setDate(5, new java.sql.Date(new Date().getTime()));

            // 执行SQL
            int count = pst.executeUpdate();
            if (count > 0) {
                System.out.println("添加成功");
            } else {
                System.out.println("添加失败");
            }

        } catch (SQLException e) {
            throw new RuntimeException(e);
        } finally {
            JDBCUtils.release(con, pst, null);
        }
    }
}
