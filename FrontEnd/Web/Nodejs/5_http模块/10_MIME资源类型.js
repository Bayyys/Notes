const http = require("http");
const fs = require("fs");
const path = require("path");

let mimes = {
  html: "text/html",
  css: "text/css",
  js: "text/javascript",
  png: "image/png",
  jpg: "image/jpeg",
  gif: "image/gif",
  mp4: "video/mp4",
  mp3: "audio/mp3",
  json: "application/json",
};

const server = http.createServer((request, response) => {
  // 获取请求的路径
  let { pathname } = new URL(request.url, "http://127.0.0.1");
  // 获取文件的后缀名
  let filePath = path.join(__dirname, "public", pathname);

  // 读取文件
  fs.readFile(filePath, (err, data) => {
    if (err) {
      switch (err.code) {
        case "ENOENT":
          response.statusCode = 404;
          response.end("404, 您请求的资源不存在");
          break;
        case "EPERM":
          response.statusCode = 403;
          response.end("403, 您没有权限访问该资源");
        default:
          response.statusCode = 500;
          response.end("500, 服务器内部错误");
      }
      return;
    }
    let ext = path.extname(pathname).slice(1);
    let type = mimes[ext];
    if (type) {
      if (type === "text/html") {
        response.setHeader("Content-Type", type + ";charset=utf-8");
      }
      else {
        response.setHeader("Content-Type", type);
      }
    }
    else {
      response.setHeader("Content-Type", "application/octet-stream");
    }
    response.end(data);
  });
});

server.listen(9000, () => {
  console.log("服务器启动成功了, 请访问: http://localhost:9000");
});
<tab> </tab>