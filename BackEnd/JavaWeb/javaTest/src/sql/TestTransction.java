package src.sql;

import src.sql.utils.JDBCUtils;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class TestTransction {
    public static void main(String[] args) {
        Connection con = null;
        PreparedStatement pst = null;

        try {
            con = JDBCUtils.getConnection();
            // 关闭数据库的自动提交，自动会开启事务
            con.setAutoCommit(false);   // 开启事务

            // 预编译SQL, 先写SQL, 然后不执行
            // 区别：
            // 使用？占位符代替参数
            String sql1 = "UPDATE `account` SET money=money+200 WHERE `name`=?";
            pst = con.prepareStatement(sql1);    // 获取执行SQL的对象, 预编译SQL语句
            // 手动给参数赋值
//            pst.setInt(1, 200);
            pst.setString(1, "A");
            int count = pst.executeUpdate(sql1);

            String sql2 = "UPDATE `account` SET money=money-200 WHERE `name`=?";
            pst = con.prepareStatement(sql2);    // 获取执行SQL的对象, 预编译SQL语句
//            pst.setInt(1, 200);
            pst.setString(1, "B");
            count = pst.executeUpdate(sql2);

            // 提交事务
            con.commit();
            System.out.println("转账成功");

        } catch (SQLException e) {
            // 事务回滚
            try {
                con.rollback();
            } catch (SQLException e1) {
                throw new RuntimeException(e1);
            }
            throw new RuntimeException(e);
        } finally {
            JDBCUtils.release(con, pst, null);
        }
    }
}
