<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%--
  Created by IntelliJ IDEA.
  User: BAY
  Date: 2023/7/4
  Time: 23:14
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>when 测试</title>
</head>
<body>
<%--定义一个变量score，值为85--%>
<c:set var="score" value="55"/>

<c:choose>
  <c:when test="${score>=90}">
    你的成绩为优秀
  </c:when>
  <c:when test="${score>=80}">
    你的成绩为一般
  </c:when>
  <c:when test="${score>=70}">
    你的成绩为良好
  </c:when>
  <c:when test="${score>=30}">
    你的成绩为不及格
  </c:when>
  <c:otherwise>
    你的成绩不足30分
  </c:otherwise>
</c:choose>
</body>
</html>
