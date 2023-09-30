const express = require("express");
const app = express();

app.get("admin", (req, res) => {
  // // 原生响应
  // res.statusCode = 200; // 设置响应状态码
  // res.statusMessage = "OK"; // 设置响应状态信息
  // res.setHeader("Content-Type", "text/html;charset=utf-8"); // 设置中文编码
  // res.write("<h1>你好, 世界!</h1>");  // 设置响应体(写入响应体)
  // res.end("response");  // 设置响应体(结束响应)

  // // express 响应
  // res.status(200) // 设置响应状态码
  // res.set('a', '1') // 设置响应头
  // res.send('<h1>你好, 世界!</h1>') // 设置响应体(express 会自动设置中文编码)

  // // 链式调用
  // res.status(200).set('a', '1').send('<h1>你好, 世界!</h1>')

  // 其他响应方法
  res.redirect('http://www.baidu.com') // 重定向(url, 默认状态码 302)
  res.download('./package.json') // 下载文件(Content-Disposition: attachment; filename=package.json)
  res.sendFile(__dirname + '/post.html') // 发送文件(文件路径, 回调函数)
  res.json({ name: 'zs' }) // 发送 json 数据(Content-Type: application/json)
});

app.listen(8000, () => {
  console.log(
    "服务已经启动(8000端口监听中...), 请访问: http://localhost:8000/response"
  );
});
