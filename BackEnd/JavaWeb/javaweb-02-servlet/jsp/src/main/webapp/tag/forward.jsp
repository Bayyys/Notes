<%--
  Created by IntelliJ IDEA.
  User: BAY
  Date: 2023/7/4
  Time: 22:26
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>forward (used by jsptag.jsp)</title>
</head>
<body>
<h2>
    This is the forwarded page.
</h2>

<h3>
    (EL表达式) 测试取参数：name=${param.name}, age=${param.age}
</h3>
<h3>
    (JSP脚本) 测试取参数：
        名字: <%=request.getParameter("name")%>
        年龄: <%=request.getParameter("age")%>

</h3>
</body>
</html>
