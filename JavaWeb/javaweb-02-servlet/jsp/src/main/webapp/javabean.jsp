<%--
  Created by IntelliJ IDEA.
  User: BAY
  Date: 2023/7/5
  Time: 21:38
  To change this template use File | Settings | File Templates.
--%>
<%@page import="com.bayyy.entity.People" %>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>JavaBean 测试</title>
</head>
<body>
<%
//    People people = new People();
//    people.setId(1);
//    people.setName("Bay");
//    people.setAge(18);
//    people.setAddress("China");
%>

<jsp:useBean id="people" class="com.bayyy.entity.People" scope="page"/>

<jsp:setProperty name="people" property="id" value="1"/>
<jsp:setProperty name="people" property="name" value="Bay"/>
<jsp:setProperty name="people" property="age" value="18"/>
<jsp:setProperty name="people" property="address" value="China"/>

id：<jsp:getProperty name="people" property="id"/>
姓名：<jsp:getProperty name="people" property="name"/>
年龄：<jsp:getProperty name="people" property="age"/>
地址：<jsp:getProperty name="people" property="address"/>

</body>
</html>
