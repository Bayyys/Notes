<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ page errorPage="/error/error500.jsp" %>
<html>
<body>
<h1>JSP基础语法</h1>

<%--注释--%>
<%--JSP表达式
  作用：用来将程序的输出，输出到客户端
  <%= 变量或者表达式%>
  --%>
<%= new java.util.Date()%>
<% int j = 5/0;%>

<hr>    <%--分割线--%>

<%--JSP脚本
  作用：用来定义java代码
  <% java代码 %>
  --%>
<%
    int sum = 0;
    for (int i = 0; i < 10; i++) {
        sum += i;
    }
    out.println("<h1>Sum = " + sum + "</h1>");
%>

<hr>

<%--JSP脚本片段再实现
    作用：可以拆开书写
    <%! java代码 %>
    --%>
<%! int sum = 0; %>
<p>定义了sum=0;</p>
<% for (int i = 0; i < 10; i++) {
    sum += i;
} %>
<h1>Sum = <%= sum %></h1>



</body>
</html>
