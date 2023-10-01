var express = require("express");
var router = express.Router();
var formidable = require("formidable");
const path = require("path");

/* GET home page. */
router.get("/", function (req, res, next) {
  res.render("index", { title: "Express" });
});

// 显示上传表单
router.get("/portrait", function (req, res, next) {
  res.render("portrait"); // 渲染模板 portrait.ejs
});

// 处理文件上传
router.post("/portrait", function (req, res, next) {
  const form = formidable({
    multiples: true, // 多文件上传
    uploadDir: path.join(__dirname, "../public/images"), // 上传目录
    keepExtensions: true, // 保留后缀
  });

  form.parse(req, (err, fields, files) => {
    if (err) {
      next(err);
      return;
    }
    res.send("<h1>上传成功</h1>");
    return;
  });
  res.send("<h1>上传失败</h1>");
});

module.exports = router;
