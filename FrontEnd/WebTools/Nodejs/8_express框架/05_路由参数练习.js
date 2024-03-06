const express = require("express");
const app = express();

// 导入 json 数据
const { singers } = require("./singers.json");

app.get("/singer/:id.html", (req, res) => {
  let id = req.params.id;
  // let {id} = req.params; // 结构赋值
  // 在 singers 数组中找到 id 对应的歌手信息
  let singer = singers.find((item) => item.id == id);
  if (!singer) {
    res.statusCode = 404;
    res.end("<h1>404 Not Found</h1>");
    return;
  }

  res.end(`
  <!DOCTYPE html>
  <html lang="en">
  <head>
    <meta charset="UTF-8" />
  </head>
  <body>
    <h1>歌手: ${singer.name}</h1>
    <h2>性别: ${singer.sex}</h2>
  </body>
  <script></script>
  </html>
  `);
});

app.listen(8000, () => {
  console.log(
    "服务已经启动(8000端口监听中...), 请访问: http://localhost:8000/singer"
  );
});
