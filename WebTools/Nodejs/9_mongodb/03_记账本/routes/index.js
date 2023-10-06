var express = require("express");
var router = express.Router();
const path = require("path");
// 导入 lowdb
const low = require("lowdb");
const FileSync = require("lowdb/adapters/FileSync");
const adapter = new FileSync(path.join(__dirname, "/../data/db.json"));
const db = low(adapter); // 获取数据库实例
const shortid = require("shortid"); // 用于生成 id
const moment = require("moment"); // 用于格式化时间
const AccountModel = require("../models/AccountModel");

// 记账本列表
router.get("/account", function (req, res, next) {
  AccountModel.find()
    .sort({ time: -1 })
    .then((data) => {
      res.render("list", {
        accounts: data,
        moment,
      });
    })
    .catch((err) => {});
});

// 删除账单
router.get("/account/:id", function (req, res, next) {
  AccountModel.deleteOne({ _id: req.params.id })
    .then((data) => {
      res.render("success", { msg: "删除成功~", url: "/account" });
    })
    .catch((err) => {
      res.render("error", { msg: "删除失败~", url: "/account" });
    });
});

// 创建账单页面
router.get("/create", function (req, res, next) {
  res.render("create");
});

// 新账单添加
router.post("/success", (req, res) => {
  console.log(req.body);
  AccountModel.create({
    ...req.body,
    time: moment(req.body.time).toDate(), // 将时间字符串转换为时间对象, 解构赋值后新增同属性会覆盖
  }).then((data) => {
    console.log(data);
  });
  res.render("success", { msg: "添加成功~", url: "/account" });
});

module.exports = router;
