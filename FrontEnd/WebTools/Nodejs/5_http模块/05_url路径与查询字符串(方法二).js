const http = require("http");

const server = http.createServer((request, response) => {
  let url = new URL(request.url, "http://localhost:9000");
  console.log(url);
  // url.pathname 表示 url 路径
  console.log(url.pathname);
  // url.searchParams.get() 方法可以获取查询字符串
  console.log(url.searchParams.get("keyword"));

  response.setHeader("content-type", "text/html;charset=utf-8");
  response.end("url路径与查询字符串!");
});

server.listen(9000, () => {
  console.log("服务器启动成功了, 请访问: http://localhost:9000");
});
