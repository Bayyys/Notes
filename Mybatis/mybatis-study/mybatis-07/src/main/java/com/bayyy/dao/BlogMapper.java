package com.bayyy.dao;

import com.bayyy.pojo.Blog;

import java.util.HashMap;
import java.util.List;

public interface BlogMapper {
    // 查询所有博客
    List<Blog> selectAllBlog();

    // 插入博客
    int addBlog(Blog blog);

    // 查询博客
    List<Blog> selectBlogIf(HashMap map);
}
