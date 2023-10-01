// 1. 导入 express
const express = require("express");

// 2. 创建路由对象
const router = express.Router();

// 3. 创建路由规则

router.get("/home", (req, res) => {
  res.send("<h1>首页</h1>");
});

router.get("/search", (req, res) => {
  res.send("<h1>内容搜索</h1>");
});

// 4. 暴露路由对象
module.exports = router;
