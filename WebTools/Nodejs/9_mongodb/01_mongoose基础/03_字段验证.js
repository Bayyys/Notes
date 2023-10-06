const mongoose = require("mongoose");

mongoose.connect("mongodb://127.0.0.1:27017/users");

mongoose.connection.once("open", () => {
  const BookSchema = new mongoose.Schema({
    name: {
      type: String,
      required: true, // 必要的
    },
    author: {
      type: String,
      default: "匿名", // 默认值
    },
    price: {
      type: Number,
      enum: [20, 30, 40], // 枚举
    },
    boolID: {
      type: Number,
      unique: true, // 唯一值
    },
  });
  const BookModel = mongoose.model("book", BookSchema);
  BookModel.create({
    name: "西游记",
    author: "吴承恩",
    price: 100,
  })
    .then((data) => {
      console.log(data);
      mongoose.disconnect(); // 关闭数据库连接
    })
    .catch((err) => {
      console.log("err", err);
    });
});
mongoose.connection.on("error", () => {
  console.log("数据库连接失败");
});
mongoose.connection.once("close", () => {
  console.log("数据库断开连接");
});
