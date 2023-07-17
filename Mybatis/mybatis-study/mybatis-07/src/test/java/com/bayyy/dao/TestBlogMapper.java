package com.bayyy.dao;

import com.bayyy.pojo.Blog;
import com.bayyy.utils.IDUtils;
import com.bayyy.utils.MyBatisUtils;
import org.apache.ibatis.session.SqlSession;
import org.junit.Test;

import java.util.Date;
import java.util.HashMap;

public class TestBlogMapper {
    @Test
    public void testSelectAllBlog() {
        try (SqlSession sqlSession = MyBatisUtils.getSqlSession()) {
            sqlSession.getMapper(BlogMapper.class).selectAllBlog().forEach(System.out::println);
        }
    }

    @Test
    public void testAddBolg() {
        try (SqlSession sqlSession = MyBatisUtils.getSqlSession()) {
            BlogMapper mapper = sqlSession.getMapper(BlogMapper.class);

            Blog blog = new Blog();
            blog.setId(IDUtils.getId());
            blog.setTitle("Mybatis如此简单");
            blog.setAuthor("Bayyy");
            blog.setCreateTime(new Date());
            blog.setViews(9999);
            mapper.addBlog(blog);

            blog.setId(IDUtils.getId());
            blog.setTitle("Java如此简单");
            mapper.addBlog(blog);

            blog.setId(IDUtils.getId());
            blog.setTitle("Spring如此简单");
            mapper.addBlog(blog);

            blog.setId(IDUtils.getId());
            blog.setTitle("微服务如此简单");
            mapper.addBlog(blog);
        }
    }

    @Test
    public void testSelectBlogIf() {
        try (SqlSession sqlSession = MyBatisUtils.getSqlSession()) {
            BlogMapper mapper = sqlSession.getMapper(BlogMapper.class);

            HashMap map = new HashMap();
            map.put("author", "Bayyy");
            map.put("title", "Mybatis如此简单");
            mapper.selectBlogIf(map).forEach(System.out::println);


            Blog blog = new Blog();
            blog.setAuthor("Bayyy");
//            blog.setTitle("Mybatis如此简单");
//            mapper.selectBlogIf(blog).forEach(System.out::println);
        }
    }
}
