import com.bayyy.pojo.People;
import com.bayyy.pojo.Student;
import com.bayyy.pojo.User;
import org.junit.Test;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class MyTest {
    @Test
    public void test1() {
        ClassPathXmlApplicationContext context = new ClassPathXmlApplicationContext("beans.xml");
//        Student student = (Student) context.getBean("student");
//        System.out.println(student.toString());

        User user1 = context.getBean("user1", User.class);
        System.out.println(user1.toString());
        User user2 = context.getBean("user2", User.class);
        System.out.println(user2.toString());
    }

    @Test
    public void test2() {
        ClassPathXmlApplicationContext context = new ClassPathXmlApplicationContext("beans.xml");
        People people = context.getBean("people", People.class);
        System.out.println(people.toString());
        people.getCat().shout();
        people.getDog().shout();
    }
}
