<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<body>
<h1>登录</h1>

<div style="text-align: center">
    <%-- 以post方式提交表单 --%>
    <form action="${pageContext.request.contextPath}/login" method="post">
        用户名:<input type="text" name="usename"> <br>
        密码:<input type="password" name="password"> <br>
        爱好:
        <input type="checkbox" name="hobbys" value="sing">唱歌
        <input type="checkbox" name="hobbys" value="dance">跳舞
        <input type="checkbox" name="hobbys" value="basketball">打篮球
        <input type="checkbox" name="hobbys" value="girl">女孩 <br>
        <input type="submit">
    </form>
</div>
</body>
</html>
