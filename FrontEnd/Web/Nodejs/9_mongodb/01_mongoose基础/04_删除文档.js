const mongoose = require("mongoose");

mongoose.connect("mongodb://127.0.0.1:27017/users");

mongoose.connection.once("open", () => {
  const BookSchema = new mongoose.Schema({
    name: String,
    author: String,
    price: Number,
  });
  const Book = mongoose.model("book", BookSchema);
  Book.find({ price: { $lt: 100 } }).then((data) => {
    console.log("price search", data);
  });
  Book.find({ $or: [{ price: 100 }, { name: "三国演义" }] }).then((data) => {
    console.log("or search", data);
  });
  Book.find({ name: /三/ }).then((data) => {
    console.log("re search", data);
  });
  Book.find({ name: new RegExp("红") }).then((data) => {
    console.log("RegExp search", data);
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
