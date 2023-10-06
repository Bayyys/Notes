var express = require("express");
var router = express.Router();
const path = require("path");
const moment = require("moment"); // 用于格式化时间
const AccountModel = require("../../models/AccountModel");

// 记账本列表
router.get("/account", function (req, res, next) {
  AccountModel.find()
    .sort({ time: -1 })
    .then((data) => {
      // json格式返回
      res.json({
        code: "0000", // 状态码: 一般以20000或者0000表示成功
        msg: "读取成功", // 提示信息
        data: data, // 返回的数据
      });
    })
    .catch((err) => {
      res.json({
        code: "1001",
        msg: "读取失败",
        data: null,
      });
    });
});

// 新增记录
router.post("/account", (req, res) => {
  console.log(req.body);
  AccountModel.create({
    ...req.body,
    time: moment(req.body.time).toDate(), // 将时间字符串转换为时间对象, 解构赋值后新增同属性会覆盖
  })
    .then((data) => {
      res.json({
        code: "0000",
        msg: "添加成功",
        data: data,
      });
    })
    .catch((err) => {
      res.json({
        code: "1002",
        msg: "添加失败",
        data: null,
      });
    });
});

// 删除账单
router.delete("/account/:id", function (req, res, next) {
  AccountModel.deleteOne({ _id: req.params.id })
    .then((data) => {
      res.json({
        code: "0000",
        msg: "删除成功",
        data: data,
      });
    })
    .catch((err) => {
      res.json({
        code: "1003",
        msg: "删除失败",
        data: null,
      });
    });
});

// 获取单个账单信息
router.get("/account/:id", function (req, res, next) {
  AccountModel.findById(req.params.id)
    .then((data) => {
      res.json({
        code: "0000",
        msg: "读取成功",
        data: data,
      });
    })
    .catch((err) => {
      res.json({
        code: "1004",
        msg: "读取失败",
        data: null,
      });
    });
});

// 更新账单信息
router.patch("/account/:id", function (req, res, next) {
  AccountModel.updateOne({ _id: req.params.id }, req.body)
    .then((data) => {
      res.json({
        code: "0000",
        msg: "更新成功",
        data: data,
      });
    })
    .catch((err) => {
      res.json({
        code: "1005",
        msg: "更新失败",
        data: null,
      });
    });
});

module.exports = router;
