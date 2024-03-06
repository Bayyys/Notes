const express = require("express");
// 导入路由模块
const homeRouter = require("./routes/homeRouter");
const adminRouter = require("./routes/adminRouter");
const app = express();

// 使用路由中间件
app.use(homeRouter, adminRouter);

app.all("*", (req, res) => {
  res.status(404).send("<h1>404 Not Found</h1>");
});

app.listen(8000, () => {
  console.log(
    "服务已经启动(8000端口监听中...), 请访问: http://localhost:8000/"
  );
});
