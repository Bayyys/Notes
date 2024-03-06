<%--
  Created by IntelliJ IDEA.
  User: BAY
  Date: 2023/7/4
  Time: 22:50
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<html>
<head>
    <title>if 测试</title>
</head>
<body>
<h4>if 测试</h4>
<hr>

<%-- action: 表示提交的地址，method: 表示提交的方式 --%>
<form action="coreif.jsp" method="get">
    <%--
    EL 表达式 获取表单中的数据
    ${param.参数名}
    --%>
    <input type="text" name="usename" value="${param.usename}">
    <input type="submit" value="登录">
</form>

<%-- 判断如果提交用户名是管理员, 则登录成功 --%>
<c:if test="${param.usename == 'root'}" var="isRoot" scope="page">
    <c:out value="登陆成功"/>
</c:if>
</body>
</html>
