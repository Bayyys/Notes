const express = require("express");
const app = express();

app.get("/home", (req, res) => {
  res.end("<h1>HOME</h1>");
});

app.get("/", (req, res) => {
  res.end("<h1>ROOT</h1>");
});

app.post("/post", (req, res) => {
  res.end("<h1>Post Method</h1>");
});

app.all("/all", (req, res) => {
  res.end("<h1>ALL</h1>");
});

app.all('*', (req, res) => {
  res.end("<h1>404 Not Found</h1>");
});

app.listen(8000, () => {
  console.log(
    "服务已经启动(8000端口监听中...), 请访问: http://localhost:8000/"
  );
});
