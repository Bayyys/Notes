const http = require("http");
const fs = require("fs");

const server = http.createServer((request, response) => {
  response.setHeader("content-type", "text/html;charset=utf-8");
  let data = fs.readFileSync("./08_http响应练习.html");
  response.end(data);
});

server.listen(9000, () => {
  console.log("服务器启动成功了, 请访问: http://localhost:9000");
});
