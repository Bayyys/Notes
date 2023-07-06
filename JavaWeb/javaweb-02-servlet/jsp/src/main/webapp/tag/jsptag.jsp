<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<body>
<%@ page  %>
<h2>JSP 标签</h2>

<jsp:include page="include.jsp"></jsp:include>

<jsp:forward page="forward.jsp">
    <jsp:param name="name" value="bayyy"></jsp:param>
    <jsp:param name="age" value="24"></jsp:param>
</jsp:forward>
</body>
</html>
