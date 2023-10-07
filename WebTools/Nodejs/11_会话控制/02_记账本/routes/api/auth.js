var express = require("express");
var router = express.Router();
const UserModel = require("../../models/UserModel");
const md5 = require("md5");
const jwt = require("jsonwebtoken");
const { secret } = require("../../config/config");

// POST 登录
router.post("/login", (req, res) => {
  console.log(req.body);
  let { username, password } = req.body;
  UserModel.findOne({ username: username, password: md5(password) })
    .then((data) => {
      if (!data) {
        return res.json({
          code: "2002",
          msg: "用户名或密码错误",
          data: null,
        });
      } else {
        res.json({
          code: "0000",
          msg: "登录成功",
          data: jwt.sign(
            {
              username: data.username,
              _id: data._id,
            },
            secret,
            {
              expiresIn: 60 * 60 * 24 * 7, // 7天
            }
          ),
        });
        res.render("success", { msg: "登录成功", url: "/account" });
      }
    })
    .catch((err) => {
      res.status(500).send("登录, 请稍后再试~~");
      res.json({
        code: "2001",
        msg: "数据库读取失败",
        data: null,
      });
      return;
    });
});

// GET 退出登录
router.post("/logout", (req, res) => {
  console.log("------------------------");
  req.session.destroy((err) => {
    if (err) {
      res.render("error", { msg: "退出登录失败", url: "/login" });
    } else {
      res.render("success", { msg: "退出登录成功", url: "/login" });
    }
  });
});

module.exports = router;
