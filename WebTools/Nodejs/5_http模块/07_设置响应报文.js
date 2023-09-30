const http = require("http");

const server = http.createServer((request, response) => {
  response.statusCode = 404;  // 设置响应状态码
  response.statusMessage = "Not Found"; // 设置响应状态信息
  response.setHeader("a", "1"); // 设置响应头
  response.setHeader("content-type", "text/html;charset=utf-8");
  response.write("hello ");
  response.write("world");
  response.write("!");
  response.end("设置响应报文!");
});

server.listen(9000, () => {
  console.log("服务器启动成功了, 请访问: http://localhost:9000");
});
