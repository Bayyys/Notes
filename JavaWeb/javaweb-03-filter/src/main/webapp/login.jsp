<%--
  Created by IntelliJ IDEA.
  User: BAY
  Date: 2023/7/6
  Time: 21:47
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>

<style>
    form {
        margin-top: 50px;
        background-color: mediumpurple;
    }

    input {
        margin: 10px;
        background-color: orange;
    }

</style>
<head>
    <title>登录</title>
</head>
<body>

<form action="${pageContext.request.contextPath}/servlet/login" method="post">
    用户名: <input type="text" name="username">
    <br>
    &emsp;密码: <input type="password" name="password">
    <br>
    <input type="submit">
</form>

</body>
</html>
