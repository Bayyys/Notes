const mongoose = require("mongoose");

mongoose.connect("mongodb://127.0.0.1:27017/users");

mongoose.connection.once("open", () => {
  const BookSchema = new mongoose.Schema({
    name: String,
    author: String,
    price: Number,
  });
  const Book = mongoose.model("book", BookSchema);
  Book.find({ price: { $gt: 0 } })
    .select({ name: 1, price: 1, _id: 0 })
    .sort({ price: 1 }) // 1: 升序; -1: 降序
    .skip(1) // 跳过条数 (1条)
    .limit(2) // 限制显示条数 (3条)
    .then((data) => {
      console.log("price search", data);
    });
});
mongoose.connection.on("error", () => {
  console.log("数据库连接失败");
});
mongoose.connection.once("close", () => {
  console.log("数据库断开连接");
});
setTimeout(() => {
  mongoose.disconnect();
}, 1000);
