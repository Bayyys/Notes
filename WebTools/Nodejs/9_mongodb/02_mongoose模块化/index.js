// 导入 db 文件
const db = require("./db/db");
const BookModel = require("./models/BookModel");
const mongoose = require("mongoose");

// 调用 db 函数
db(
  () => {
    BookModel.find({ price: { $gt: 0 } })
      .select({ name: 1, price: 1, _id: 0 })
      .sort({ price: 1 }) // 1: 升序; -1: 降序
      .skip(1) // 跳过条数 (1条)
      .limit(2) // 限制显示条数 (3条)
      .then((data) => {
        console.log("price search", data);
      });
  },
  () => {
    console.log("数据库连接失败....");
  }
);
