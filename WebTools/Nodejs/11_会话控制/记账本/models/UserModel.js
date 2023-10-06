const mongoose = require("mongoose");

// 创建文档的结构对象
const UserSchema = new mongoose.Schema({
  username: String,
  password: String,
});

// 创建 model 对象
const User = mongoose.model("user", UserSchema);

// 暴露模型对象
module.exports = User;
