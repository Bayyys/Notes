// 导入模块语句 - require, 类似于 Java中的import
const http = require('http');

// 1. 创建一个httpserver服务
http.createServer(function (request, response) {
    // 告诉浏览器返回的内容类型
    response.writeHead(200, {'Content-Type': 'text/plain'});    // 以 'text/plain' 解析
    // 给浏览器输出内容
    response.end('Hello World!');
}).listen(8888);    // 2. 监听端口:8888
console.log('Server running at http://localhost:8888/');
// 3. 启动服务 node httpserver.js
// 4. 访问服务 http://localhost:8080