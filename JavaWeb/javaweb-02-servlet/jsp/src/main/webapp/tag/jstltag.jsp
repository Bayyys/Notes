<%--
  Created by IntelliJ IDEA.
  User: BAY
  Date: 2023/7/4
  Time: 22:39
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>  <%-- 引入JSTL标签库 --%>
<html>
<head>
    <title>JSTL 标签</title>
</head>
<body>
<c:if test="${param.name == 'admin'}">
    <h2>欢迎管理员</h2>
</body>
</html>
