const express = require("express");
const app = express();

app.get("/:id.html", (req, res) => {  // :id 占位符, 表示一个变量
  console.log(req.params.id);  // 123
  res.setHeader("Content-Type", "text/html;charset=utf-8"); // 设置中文编码
  res.end(`<h1>请求参数为: ${req.params.id}</h1>`);
});

app.listen(8000, () => {
  console.log(
    "服务已经启动(8000端口监听中...), 请访问: http://localhost:8000/request"
  );
});