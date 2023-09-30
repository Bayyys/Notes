const http = require('http');

const server = http.createServer((request, response) => {
  // 1. 获取请求方式
  console.log(request.method);
  // 2. 获取请求地址
  console.log(request.url); // 只包含 url 中的路径与查询字符串
  // 3. 获取HTTP协议的版本号
  console.log(request.httpVersion);
  // 4. 获取请求头信息
  console.log(request.headers);

  // 设置响应体
  response.end("Hello Server!");
});

server.listen(9000, () => {
  console.log("服务器启动成功了, 请访问: http://localhost:9000");
});