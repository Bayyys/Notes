const express = require("express");
const app = express();

app.get("/request", (req, res) => {

  // 原生方法
  console.log("method: ", req.method);  // 请求方法
  console.log("url: ", req.url);     // 请求地址
  console.log("httpVersion: ", req.httpVersion)  // http版本
  console.log("headers: ", req.headers);  // 请求头
  // express 封装的方法
  console.log("path: ", req.path);  // 请求路径(不包含请求参数)
  console.log("query: ", req.query);  // 请求参数
  console.log("params: ", req.params);  // 路由参数
  console.log("ip: ", req.ip);  // 请求ip
  console.log("get(): ", req.get("host"));  // 获取请求头中的某个字段
  console.log("hostname: ", req.hostname);  // 请求主机名
  console.log("protocol: ", req.protocol);  // 请求协议
  console.log("secure: ", req.secure);  // 请求协议是否是https
  res.end("<h1>HOME</h1>");
});

app.listen(8000, () => {
  console.log(
    "服务已经启动(8000端口监听中...), 请访问: http://localhost:8000/request"
  );
});
