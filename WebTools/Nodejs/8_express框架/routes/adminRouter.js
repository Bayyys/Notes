// 1. 导入 express
const express = require("express");

// 2. 创建路由对象
const router = express.Router();

// 3. 创建路由规则

router.get("/admin", (req, res) => {
  res.send("<h1>后台管理</h1>");
});

router.get("/setting", (req, res) => {
  res.send("<h1>设置</h1>");
});

// 4. 暴露路由对象
module.exports = router;
