// 1. 导入 mongoose 第三方模块
const mongoose = require("mongoose");

// 2. 连接 MongoDB 数据库
mongoose.connect("mongodb://127.0.0.1:27017/users");

// 3. 设置回调
// 语法: mongoose.connection.on("事件名称", 回调函数)
// 或者: mongoose.connection.once("事件名称", 回调函数) => 只执行一次, 适合写连接成功的回调
// 事件名称:
// 1. open => 连接成功; 2. error => 连接失败; 3. close => 断开连接
mongoose.connection.once("open", () => {
  console.log("数据库连接成功");
});
mongoose.connection.on("error", () => {
  console.log("数据库连接失败");
});
mongoose.connection.once("close", () => {
  console.log("数据库断开连接");
});

// 4. 关闭数据库连接
setTimeout(() => {
  mongoose.disconnect();
}, 2000);
