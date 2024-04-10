const mongoose = require("mongoose");

// 创建文档的结构对象
const AccountSchema = new mongoose.Schema({
  title: {
    type: String,
    required: true,
  },
  time: {
    type: Date,
    default: Date.now(),
  },
  type: {
    type: Number,
    enum: [-1, 1],
    default: -1,
  },
  account: {
    type: Number,
    required: true,
  },
  remarks: {
    type: String,
  },
});

// 创建 model 对象
const Account = mongoose.model("account", AccountSchema);

// 暴露模型对象
module.exports = Account;
