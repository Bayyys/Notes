const express = require("express");

const app = express();

app.get("/home", (req, res) => {
  res.send("<h1>首页</h1>");
});

// 路由中间件
// 位置: 添加在路由处理函数之前
let checkCodeMiddlerware = (req, res, next) => {
  if (req.query.code === "521") {
    next();
  } else {
    res.send("<h1>请先登录</h1>");
  }
};


app.get("/admin", checkCodeMiddlerware ,(req, res) => {
  res.send("<h1>后台管理</h1>");
});

app.get("/setting", checkCodeMiddlerware, (req, res) => {
  res.send("<h1>设置</h1>");
});

app.all("*", (req, res) => {
  res.status(404).send("<h1>404 Not Found</h1>");
});

app.listen(8000, () => {
  console.log(
    "服务已经启动(8000端口监听中...), 请访问: http://localhost:8000/"
  );
});
