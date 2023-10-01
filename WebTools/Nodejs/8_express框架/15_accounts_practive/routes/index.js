var express = require("express");
var router = express.Router();
const path = require("path");
// 导入 lowdb
const low = require("lowdb");
const FileSync = require("lowdb/adapters/FileSync");
const adapter = new FileSync(path.join(__dirname, "/../data/db.json"));
const db = low(adapter); // 获取数据库实例
const shortid = require("shortid"); // 用于生成 id

// 记账本列表
router.get("/account", function (req, res, next) {
  res.render("list", { accounts: db.get("accounts").value() });
});

// 删除账单
router.get("/account/:id", function (req, res, next) {
  db.get('accounts').remove({ id: req.params.id }).write()
  res.render("success", { msg: "删除成功~", url: "/account" });
});

// 创建账单
router.get("/create", function (req, res, next) {
  res.render("create");
});

// 创建提示
router.post("/success", (req, res) => {
  const id = shortid.generate();
  db.get("accounts")
    .unshift({ id, ...req.body })
    .write();
  res.render("success", { msg: "添加成功~", url: "/account" });
});

module.exports = router;
