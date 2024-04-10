package com.bayyy.service;

import com.bayyy.dao.BookMapper;
import com.bayyy.pojo.Books;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class BookServiceImpl implements BookService{
    @Autowired
    private BookMapper bookMapper;

    public void setBookMapper(BookMapper bookMapper) {
        this.bookMapper = bookMapper;
    }

    @Override
    public int addBook(Books books) {
        return this.bookMapper.addBook(books);
    }

    @Override
    public int deleteBookByID(int id) {
        return this.bookMapper.deleteBookByID(id);
    }

    @Override
    public int updateBook(Books books) {
        return this.bookMapper.updateBook(books);
    }

    @Override
    public Books queryBookByID(int id) {
        return this.bookMapper.queryBookByID(id);
    }

    @Override
    public List<Books> queryAllBook() {
        return this.bookMapper.queryAllBook();
    }

    @Override
    public Books queryBookByName(String bookName) {
        return this.bookMapper.queryBookByName(bookName);
    }
}
