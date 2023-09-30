const http = require("http");

const server = http.createServer((request, response) => {
  const request_method = request.method;
  const request_pathname = new URL(request.url, "http://localhost:9000")
    .pathname;
  // console.log(request_method, request_pathname);
  response.setHeader("content-type", "text/html;charset=utf-8"); // 设置中文
  if (request_method === "GET") {
    if (request_pathname === "/login") {
      response.end("登录页面");
    } else if (request_pathname === "/reg") {
      response.end("注册页面");
    } else {
      response.end("404");
    }
  } else {
    response.end("404");
  }
});

server.listen(9000, () => {
  console.log("服务器启动成功了, 请访问: http://localhost:9000");
});
