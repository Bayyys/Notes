const mongoose = require("mongoose");

mongoose.connect("mongodb://127.0.0.1:27017/users");

mongoose.connection.once("open", () => {
  // console.log("数据库连接成功");
  // 1. 创建文档的结构对象(schema)
  // 设置约束条件: 约束文档中的属性名和属性值的类型
  const BookSchema = new mongoose.Schema({
    name: String,
    author: String,
    price: Number,
  });
  // 2. 创建模型对象, 对文档操作的封装对象
  const BookModel = mongoose.model("book", BookSchema);
  // 3. 新增
  BookModel.create({
    name: "西游记",
    author: "吴承恩",
    price: 100,
  })
    .then((data) => {
      console.log(data);  
      mongoose.disconnect();  // 关闭数据库连接
    })
    .catch((err) => {
      console.log(err);
    });
});
mongoose.connection.on("error", () => {
  console.log("数据库连接失败");
});
mongoose.connection.once("close", () => {
  console.log("数据库断开连接");
});
