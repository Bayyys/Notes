const express = require("express");
const app = express();
const bodyParser = require("body-parser");

// GET /login: 表单页面
app.get("/login", (req, res) => {
  res.sendFile(__dirname + "/10_表单.html");
});

// 创建 json 解析器
const jsonParser = bodyParser.json();

// 创建 querystring 解析器
const urlencodedParser = bodyParser.urlencoded({ extended: false });

// POST /login: 获取用户数据
app.post("/login", urlencodedParser, (req, res) => {
  console.log(req.body); // 中间件函数会将解析后的数据放入 req.body 中 - [Object: null prototype] { username: '123', password: '123' }
  res.send("登录成功");
});

app.listen(8000, () => {
  console.log(
    "服务已经启动(8000端口监听中...), 请访问: http://localhost:8000/login"
  );
});
