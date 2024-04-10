const http = require("http");
// 1. 导入 url 模块
const url = require("url");

const server = http.createServer((request, response) => {
  console.log(request.url);
  let res = url.parse(request.url, true); // true 表示把查询字符串转换为对象
  // url.parse() 方法会把 url 路径与查询字符串分开
  console.log("url:\n", res);
  // url 路径
  console.log("url路径:\n", res.pathname);
  // 查询字符串
  console.log("查询字符串:\n", res.query.keyword);
  response.setHeader("content-type", "text/html;charset=utf-8");
  response.end("url路径与查询字符串!");
});

server.listen(9000, () => {
  console.log("服务器启动成功了, 请访问: http://localhost:9000");
});
