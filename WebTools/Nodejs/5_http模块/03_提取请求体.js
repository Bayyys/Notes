const http = require("http");

const server = http.createServer((request, response) => {
  let body = "";
  request.on("data", (chunk) => {
    body += chunk;
  });
  request.on("end", () => {
    console.log(body);
    response.setHeader("content-type", "text/html;charset=utf-8");
    response.end("获取请求体!");
  });
});

server.listen(9000, () => {
  console.log("服务器启动成功了, 请访问: http://localhost:9000");
});
