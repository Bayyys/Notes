const express = require("express");
const path = require("path");

const app = express();

app.use(express.static(path.resolve(__dirname, "./public")));

app.get("/home", (req, res) => {
  res.send("<h1>首页</h1>");
});

app.get("/admin", (req, res) => {
  res.send("<h1>后台管理</h1>");
});

app.all("*", (req, res) => {
  res.status(404).send("<h1>404 Not Found</h1>");
});

app.listen(8000, () => {
  console.log(
    "服务已经启动(8000端口监听中...), 请访问: http://localhost:8000/"
  );
});
