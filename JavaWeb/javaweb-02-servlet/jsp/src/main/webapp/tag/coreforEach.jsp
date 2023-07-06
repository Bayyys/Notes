<%@ page import="java.util.ArrayList" %><%--
  Created by IntelliJ IDEA.
  User: BAY
  Date: 2023/7/5
  Time: 21:09
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<html>
<head>
    <title>forEach 测试</title>
</head>
<body>
<%
    ArrayList<String> people = new ArrayList<String>();
    people.add("张三");
    people.add("李四");
    people.add("王五");
    people.add("赵六");
    people.add("田七");
    request.setAttribute("list", people);
%>
<%--
var: 代表当前元素
items: 代表集合
--%>
<c:forEach var="people" items="${list}">
    <c:out value="${people}"/>
    <br/>
</c:forEach>

<c:out value="begin-end"/>
<br>

<%--
begin: 开始的索引
end: 结束的索引
step: 步长
--%>
<c:forEach begin="1" end="4" step="2" var="person" items="${list}">
    <c:out value="${person}"/>
    <br/>
</c:forEach>

</body>
</html>
