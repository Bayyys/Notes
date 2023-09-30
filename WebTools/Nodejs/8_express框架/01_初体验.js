// 1. 导入 express
const express = require("express");

// 2. 创建应用对象
const app = express();

// 3. 创建路由规则
app.get("/home", (req, res) => {
  res.end("hello express");
});

// 4. 监听端口启动服务
app.listen(8000, () => {
  console.log(
    "服务已经启动(8000端口监听中...), 请访问: http://localhost:8000/home"
  );
});
