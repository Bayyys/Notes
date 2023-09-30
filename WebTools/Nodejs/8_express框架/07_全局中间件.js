const express = require("express");
const fs = require("fs");
const path = require("path");

const ws = fs.createWriteStream(path.resolve(__dirname, "./log.txt"), {
  flags: "a",
});

// 创建应用对象
const app = express();

// 声明中间件函数
// function recordMiddleware(req, res, next) {...}
// == 注意要加入 next 参数 == 
function recordMiddleware(req, res, next) {
  let { url, ip } = req;
  let time = new Date().toLocaleString();
  let log = `url: ${url}, ip: ${ip}, time: ${time}\n`;
  ws.write(log);
  next(); // 调用下一个中间件函数
}

// 使用中间件函数
app.use(recordMiddleware);


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
