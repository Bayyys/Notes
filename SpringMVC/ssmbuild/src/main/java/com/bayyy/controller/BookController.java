package com.bayyy.controller;

import com.bayyy.pojo.Books;
import com.bayyy.service.BookService;
import org.apache.ibatis.annotations.Param;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;

import java.util.ArrayList;
import java.util.List;

@Controller
@RequestMapping("/book")
public class BookController {
    // controller 调用 service 层
    @Autowired
    @Qualifier("bookServiceImpl")
    private BookService bookService;


    // 查询全部的书籍，并且返回到一个书籍展示页面
    @RequestMapping("/allBook")
    public String list(Model model) {
        List<Books> books = bookService.queryAllBook();
        model.addAttribute("list", books);
        return "allBook";
    }

    // 跳转到增加书籍页面
    @RequestMapping("/toAddBook")
    public String toAddBook() {
        return "toAddBook";
    }

    // 添加书籍的请求
    @RequestMapping("/addBook")
    public String addBook(Books books) {
        bookService.addBook(books);
        return "redirect:/book/allBook";
    }

    // 跳转到修改书籍页面
    @RequestMapping("/toUpdateBook/{bookId}")
    public String toUpdateBook(@PathVariable("bookId") int bookId, Model model) {
        Books book = bookService.queryBookByID(bookId);
        System.out.println(book);
        model.addAttribute("book", book);
        return "toUpdateBook";
    }

    // 修改书籍
    @RequestMapping("/updateBook")
    public String updateBook(Books books) {
        bookService.updateBook(books);
        return "redirect:/book/allBook";
    }

    // 删除书籍
    @RequestMapping("/del/{bookId}")
    public String deleteBookById(@PathVariable("bookId") int bookId) {
        bookService.deleteBookByID(bookId);
        return "redirect:/book/allBook";
    }

    // 查询书籍
    @RequestMapping("/queryBook")
    public String queryBookByName(@Param("queryBookName") String queryBookName, Model model) {
        if (queryBookName.equals("")) {
            model.addAttribute("error", "未查到");
            return "allBook";
        }
        Books books = bookService.queryBookByName(queryBookName);
        ArrayList<Books> list = new ArrayList<Books>();
        list.add(books);
        if (books == null) {
            list = (ArrayList<Books>) bookService.queryAllBook();
            model.addAttribute("error", "未查到");
        }
        model.addAttribute("list", list);
        return "allBook";
    }

}
