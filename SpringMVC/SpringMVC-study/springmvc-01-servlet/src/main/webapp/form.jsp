<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>Form</title>
</head>
<body>
<form action="<c:url value="/hello"/>" method="post">
    <input type="text" name="method" value="name">
    <input type="submit" value="submit">
</form>
</body>
</html>
