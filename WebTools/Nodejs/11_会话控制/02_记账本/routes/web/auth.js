var express = require("express");
var router = express.Router();
const UserModel = require("../../models/UserModel");
const md5 = require("md5");

// GET 注册
router.get("/reg", (req, res) => {
  // 响应 HTML 页面
  res.render("auth/reg");
});

// POST 注册
router.post("/reg", (req, res) => {
  UserModel.create({
    ...req.body,
    password: md5(req.body.password),
  })
    .then((data) => {
      res.render("success", {
        msg: data.username + " 注册成功",
        url: "/login",
      });
    })
    .catch((err) => {
      res.render("success", { msg: "注册失败", url: "/login" });
    });
});

// GET 登录
router.get("/login", (req, res) => {
  // 响应 HTML 页面
  res.render("auth/login");
});

// POST 登录
router.post("/login", (req, res) => {
  let { username, password } = req.body;
  UserModel.findOne({ username: username, password: md5(password) }).then(
    (data) => {
      if (!data) {
        return res.render("success", { msg: "登录失败", url: "/login" });
      } else {
        req.session.username = data.username;
        req.session._id = data._id;
        res.render("success", { msg: "登录成功", url: "/account" });
      }
    }
  );
});

// GET 退出登录
router.post("/logout", (req, res) => {
  req.session.destroy((err) => {
    if (err) {
      res.render("error", { msg: "退出登录失败", url: "/login" });
    } else {
      res.render("success", { msg: "退出登录成功", url: "/login" });
    }
  });
});

module.exports = router;
