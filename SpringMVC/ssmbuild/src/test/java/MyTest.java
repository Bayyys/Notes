import com.bayyy.pojo.Books;
import com.bayyy.service.BookServiceImpl;
import org.junit.Test;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class MyTest {
    @Test
    public void test1() {
        ClassPathXmlApplicationContext context = new ClassPathXmlApplicationContext("applicationContext.xml");
        BookServiceImpl bookServiceImpl = context.getBean("bookServiceImpl", BookServiceImpl.class);
        for (Books book: bookServiceImpl.queryAllBook()) {
            System.out.println(book);
        }
    }
}
