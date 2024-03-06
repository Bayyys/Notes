import com.bayyy.mapper.UserMapper;
import com.bayyy.pojo.User;
import org.junit.Test;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class MyTest {
    @Test
    public void test1() {
        ClassPathXmlApplicationContext context = new ClassPathXmlApplicationContext("applicationContext.xml");
        context.getBean("userMapper", UserMapper.class).selectUser().forEach(System.out::println);
    }

    @Test
    public void test2() {
        ClassPathXmlApplicationContext context = new ClassPathXmlApplicationContext("applicationContext.xml");
        UserMapper mapper = context.getBean("userMapper", UserMapper.class);
        User user = context.getBean("user", User.class);
        System.out.println("添加了 " + mapper.addUser(user) + " 条数据");
        System.out.println("当前数据库中的数据为：");
        mapper.selectUser().forEach(System.out::println);
        System.out.println("删除了 " + mapper.deleteUser(5) + " 条数据");
        System.out.println("当前数据库中的数据为：");
        mapper.selectUser().forEach(System.out::println);
    }
}
