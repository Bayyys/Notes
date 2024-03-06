package com.bayyy.servlet.user;

import com.alibaba.fastjson.JSONArray;
import com.bayyy.entity.Role;
import com.bayyy.entity.User;
import com.bayyy.service.role.RoleService;
import com.bayyy.service.role.RoleServiceImpl;
import com.bayyy.service.user.UserService;
import com.bayyy.service.user.UserServiceImpl;
import com.bayyy.utils.Constants;
import com.bayyy.utils.PageSupport;
import com.mysql.cj.util.StringUtils;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.io.PrintWriter;
import java.sql.SQLException;
import java.util.HashMap;
import java.util.List;

// 实现Servlet复用
public class UserServlet extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        String method = req.getParameter("method");
        if (method.equals("savepwd")) {
            this.updatePwd(req, resp);
        } else if (method.equals("pwdmodify")) {
            this.pwdModify(req, resp);
        } else if (method.equals("query")) {
            this.query(req, resp);
        }
    }

    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        doGet(req, resp);
    }

    // 查询用户列表
    public void query(HttpServletRequest req, HttpServletResponse resp) {
        // 查询用户列表

        // 从前端获取数据
        String queryUserName = req.getParameter("queryname");
        String temp = req.getParameter("queryUserRole");
        String pageIndex = req.getParameter("pageIndex");
        int queryUserRole = 0;

        // 获取用户列表
        UserService userService = new UserServiceImpl();
        List<User> userList = null;

        // 第一次走这个请求, 一定是第一页, 页面大小固定的
        int pageSize = 5;
        int currentPageNo = 1;

        if (queryUserName == null) {
            queryUserName = "";
        }
        if (temp != null && !temp.equals("")) { // 前端获取数据出错
            queryUserRole = Integer.parseInt(temp);
        }
        if (pageIndex != null) {
            currentPageNo = Integer.parseInt(pageIndex);
        }
        System.out.println("queryUserName servlet: " + queryUserName);
        System.out.println("queryUserRole servlet: " + queryUserRole);

        // 获取用户总数(分页: 上一页, 下一页)
        int totalCount = userService.getUserCount(queryUserName, queryUserRole);
        // 总页数支持
        PageSupport pageSupport = new PageSupport();
        pageSupport.setPageSize(pageSize); // 设置页面容量
        pageSupport.setTotalCount(totalCount); // 总数量(表)
        pageSupport.setCurrentPageNo(currentPageNo); // 当前页码

        int totalPageCount = pageSupport.getTotalPageCount();

        // 控制首页和尾页
        if (currentPageNo < 1) {
            currentPageNo = 1;
        } else if (currentPageNo > totalPageCount) {
            currentPageNo = totalPageCount;
        }

        // 获取用户列表展示
        userList = userService.getUserList(queryUserName, queryUserRole, currentPageNo, pageSize);
        req.setAttribute("userList", userList);

        RoleService roleService = new RoleServiceImpl();
        List<Role> roleList = roleService.getRoleList();
        req.setAttribute("roleList", roleList);

        req.setAttribute("totalCount", totalCount);
        req.setAttribute("currentPageNo", currentPageNo);
        req.setAttribute("totalPageCount", totalPageCount);
        req.setAttribute("queryUserName", queryUserName);
        req.setAttribute("queryUserRole", queryUserRole);

        // 返回前端
        try {
            req.getRequestDispatcher("userlist.jsp").forward(req, resp);
        } catch (ServletException e) {
            throw new RuntimeException(e);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }

    }


    // 修改密码
    public void updatePwd(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        // 从Session里面获取用户信息
        Object userSession = req.getSession().getAttribute(Constants.USER_SESSION);

        String newpassword = req.getParameter("newpassword");

        boolean flag = false;

        if (userSession != null && !StringUtils.isNullOrEmpty(newpassword)) {
            UserService userService = new UserServiceImpl();
            flag = userService.updatePwd(((User) userSession).getId(), newpassword);
            if (flag) {
                req.setAttribute("message", "修改密码成功, 请退出, 使用新密码登录");
                // 密码修改成功, 移除当前Session
                req.getSession().removeAttribute(Constants.USER_SESSION);
            } else {
                req.setAttribute("message", "密码修改失败");
            }
        } else {
            req.setAttribute("message", "新密码有问题");
        }
        req.getRequestDispatcher("pwdmodify.jsp").forward(req, resp);
    }

    // 验证旧密码
    public void pwdModify(HttpServletRequest req, HttpServletResponse resp) {
        // 1. 从Session里面获取用户信息
        Object userSession = req.getSession().getAttribute(Constants.USER_SESSION);
        String oldpassword = req.getParameter("oldpassword");

        // 使用 Map
        HashMap<String, String> resultMap = new HashMap<String, String>();
        if (userSession == null) {  // Session 过期或不存在
            resultMap.put("result", "sessionerror");
        } else if (StringUtils.isNullOrEmpty(oldpassword)) {  // 旧密码输入为空
            resultMap.put("result", "error");
        } else {
            String userPassword = ((User) userSession).getUserPassword();
            if (oldpassword.equals(userPassword)) {  // 旧密码输入正确
                resultMap.put("result", "true");
            } else {  // 旧密码输入错误
                resultMap.put("result", "false");
            }
        }

        try {
            resp.setContentType("application/json");
            PrintWriter writer = resp.getWriter();
            // JSONArray 阿里巴巴的 JSON 工具类, 转换格式
            writer.write(JSONArray.toJSONString(resultMap));
            writer.flush();
            writer.close();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}