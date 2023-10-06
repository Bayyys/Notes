/**
 *
 * @param {*} success 数据库连接成功的回调函数
 * @param {*} error 数据库连接失败的回调函数
 */
module.exports = function (success, error) {
  // 如果没有传递回调函数, 则使用默认的回调函数
  if (typeof error !== "function") {
    error = () => {
      console.log("数据库连接失败");
    };
  }
  // 1. 导入 mongoose 第三方模块
  const mongoose = require("mongoose");
  const { DBHOST, DBPORT, DBNAME } = require("../config/config");

  // 2. 连接 MongoDB 数据库
  mongoose.connect(`mongodb://${DBHOST}:${DBPORT}/${DBNAME}`);

  // 3. 设置回调
  // 1. open => 连接成功; 2. error => 连接失败; 3. close => 断开连接
  mongoose.connection.once("open", () => {
    success();
  });
  mongoose.connection.on("error", () => {
    error();
  });
  mongoose.connection.once("close", () => {
    console.log("数据库断开连接");
  });
};
