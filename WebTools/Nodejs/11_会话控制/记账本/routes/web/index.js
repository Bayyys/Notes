const express = require("express");
const path = require("path");
const moment = require("moment"); // 用于格式化时间
const AccountModel = require("../../models/AccountModel");  // 引入mongoose模型
const isLogin = require("../../middlewares/isLogin"); // 引入登录中间件
// 创建路由对象
const router = express.Router();

// GET 首页
router.get("/", (req, res) => {
  res.redirect("/account");
});

// 记账本列表
router.get("/account", isLogin, function (req, res, next) {
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
router.get("/account/:id", isLogin, function (req, res, next) {
  AccountModel.deleteOne({ _id: req.params.id })
    .then((data) => {
      res.render("success", { msg: "删除成功~", url: "/account" });
    })
    .catch((err) => {
      res.render("error", { msg: "删除失败~", url: "/account" });
    });
});

// 创建账单页面
router.get("/create", isLogin, function (req, res, next) {
  res.render("create");
});

// 新账单添加
router.post("/success", isLogin, (req, res) => {
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
