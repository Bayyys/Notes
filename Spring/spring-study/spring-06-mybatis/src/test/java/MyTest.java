import com.bayyy.mapper.UserMapper;
import com.bayyy.mapper.UserMapperImpl;
import com.bayyy.pojo.User;
import com.bayyy.utils.MyBatisUtils;
import org.apache.ibatis.session.SqlSession;
import org.junit.Test;
import org.springframework.context.support.ClassPathXmlApplicationContext;

import java.util.List;

public class MyTest {
    @Test
    public void test1() {
        try (SqlSession sqlSession = MyBatisUtils.getSqlSession()) {
            UserMapper mapper = sqlSession.getMapper(UserMapper.class);
            mapper.selectUser().forEach(System.out::println);
        }
    }

    @Test
    public void test2() {
        ClassPathXmlApplicationContext context = new ClassPathXmlApplicationContext("applicationContext.xml");
        context.getBean("userMapper", UserMapper.class).selectUser().forEach(System.out::println);
    }

    @Test
    public void test3() {
        ClassPathXmlApplicationContext context = new ClassPathXmlApplicationContext("applicationContext.xml");
        context.getBean("userMapper2", UserMapper.class).selectUser().forEach(System.out::println);
    }
}
