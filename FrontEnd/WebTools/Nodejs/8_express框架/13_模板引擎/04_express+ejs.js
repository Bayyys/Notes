const express = require("express");
const ejs = require("ejs");
const fs = require("fs");
const path = require("path");

const app = express();
// 1. 设置模板引擎
app.set("view engine", "ejs");
// 2. 设置模板目录
app.set("views", path.resolve(__dirname, "views"));

app.get("/login", (req, res) => {
  let username = "bay";
  // 3. render方法渲染模板
  res.render("login", { username });
});

app.listen(8000, () => {
  console.log("http://localhost:8000");
});
