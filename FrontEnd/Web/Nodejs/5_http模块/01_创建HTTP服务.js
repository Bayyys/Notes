// 1. 引入http模块
const http = require("http");

// 2. 创建http服务
// request 请求对象, 获取客户端传递过来的信息
// response 响应对象, 给客户端发送响应信息
const server = http.createServer((request, response) => {
  response.end("Hello Server!"); // 响应信息
  //解决响应内容中文乱码的问题
  response.setHeader("content-type", "text/html;charset=utf-8");
  response.end("你好, HTTP服务器!"); // 响应信息
});

// 3. 监听端口, 启动服务
server.listen(9000, () => {
  console.log("服务器启动成功了, 请访问: http://localhost:9000");
});
