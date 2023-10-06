const mongoose = require("mongoose");

// 创建文档的结构对象
const BookSchema = new mongoose.Schema({
  name: String,
  author: String,
  price: Number,
});

// 创建 model 对象
const Book = mongoose.model("book", BookSchema);

// 暴露模型对象
module.exports = Book;
