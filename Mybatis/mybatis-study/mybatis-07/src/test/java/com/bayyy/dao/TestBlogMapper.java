package com.bayyy.dao;

import com.bayyy.pojo.Blog;
import com.bayyy.utils.IDUtils;
import com.bayyy.utils.MyBatisUtils;
import org.apache.ibatis.session.SqlSession;
import org.junit.Test;

import java.util.ArrayList;
import java.util.Date;
import java.util.HashMap;
import java.util.List;

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


    @Test
    public void testSelectBlogChoose() {
        try (SqlSession sqlSession = MyBatisUtils.getSqlSession()) {
            BlogMapper mapper = sqlSession.getMapper(BlogMapper.class);

            HashMap map = new HashMap();
//            map.put("author", "Bayyy");
//            map.put("title", "Mybatis如此简单");
            map.put("views", 9999);
            mapper.selectBlogChoose(map).forEach(System.out::println);
        }
    }

    @Test
    public void testUpdateBlogSet() {
        try (SqlSession sqlSession = MyBatisUtils.getSqlSession()) {
            BlogMapper mapper = sqlSession.getMapper(BlogMapper.class);

            HashMap map = new HashMap();
            map.put("author", "Bayyy");
            map.put("title", "Mybatis如此简单");
            map.put("id", "1");
            mapper.updateBlogSet(map);
        }
    }

    @Test
    public void testSelectBlogForeach() {
        try (SqlSession sqlSession = MyBatisUtils.getSqlSession()) {
            BlogMapper mapper = sqlSession.getMapper(BlogMapper.class);

            List<String> ids = new ArrayList<String>();
            ids.add("1");
            mapper.selectBlogForeach(ids).forEach(System.out::println);
            mapper.selectBlogForeach(ids).forEach(System.out::println);
        }
    }
}
