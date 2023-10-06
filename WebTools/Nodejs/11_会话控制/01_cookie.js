const express = require("express");
const app = express();

const cookieParser = require("cookie-parser");
app.use(cookieParser());

app.get("/", (req, res) => {
  res.send("<h1>HOME</h1>");
});

// 设置cookie
app.get("/set", (req, res) => {
  res.cookie("username", "zhangsan", {
    maxAge: 1000 * 60 * 60 * 24, // 一天
    path: "/", // 默认值
  });
  res.cookie("password", "123456");
  res.send("设置cookie成功");
});

// 删除cookie
app.get("/del", (req, res) => {
  res.clearCookie("username");
  res.send("删除cookie成功");
});

// 获取cookie
app.get("/get", (req, res) => {
  res.send(req.cookies);
});

app.listen(8000, () => {
  console.log("请访问: http://localhost:8000/");
});
