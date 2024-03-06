<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<body>
<h2>Hello World!</h2>
</body>
<%-- 通过表单上传
    get:    上传文件大小有限制，不安全
    post:   上传文件大小无限制，安全 (√)
--%>
<form action="${pageContext.request.contextPath}/upload.do" enctype="multipart/form-data" method="post">
    上传用户: <input type="text" name="username"><br>
    上传文件1: <input type="file" name="file1"><br>
    上传文件2: <input type="file" name="file2"><br>
    <p><input type="submit" value="上传"> <input type="reset" value="重置"></p>
</form>
</html>