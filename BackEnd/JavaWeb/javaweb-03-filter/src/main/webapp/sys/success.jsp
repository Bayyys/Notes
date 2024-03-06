<%--
  Created by IntelliJ IDEA.
  User: BAY
  Date: 2023/7/6
  Time: 21:38
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>

    <style>
        p, h1 {
            text-align: center;
        }
    </style>

<head>
    <title>主页</title>
</head>
<body>

<h1>主页</h1>
<hr>
<p>登录成功！<a href="../index.jsp">继续浏览...</a></p>
<p><a href="${pageContext.request.contextPath}/servlet/logout">注销</a> </p>

</body>
</html>
