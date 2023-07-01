<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%--contentType: 告诉浏览器以什么编码解析文本--%>
<html>
<body>
<h2>Hello World!</h2>

<%-- 这里超交的路径,需要寻找到项目的路径 --%>
<%-- ${pageContext. request, contextPath}代表当前的项目 --%>
<form action="${pageContext. request.contextPath}/request" method="get">
    <%-- get: 通过url传递参数 / post: 通过请求体传递参数 --%>
    用户名: <input type="text" name="username"> <br>
    密码: <input type="password" name="password"> <br>
    <input type="submit">
</form>

</body>
</html>
