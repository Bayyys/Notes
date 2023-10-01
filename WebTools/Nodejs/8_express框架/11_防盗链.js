const express = require("express");
const path = require("path");

const app = express();

// 声明中间件
app.use((req, res, next) => {
  // 检测请求头中的 referer 字段
  const referer = req.get("referer");
  if (referer) {
    let url = new URL(referer);
    let hostname = url.hostname;
    if (hostname !== "localhost") {
      res.statusCode(404).send("<h1>404 Not Found</h1>");
      return;
    }
  }
  next();
});

app.use(express.static(path.resolve(__dirname, "./public")));

app.all("*", (req, res) => {
  res.status(404).send("<h1>404 Not Found</h1>");
});

app.listen(8000, () => {
  console.log(
    "服务已经启动(8000端口监听中...), 请访问: http://127.0.0.1:8000/"
  );
});
