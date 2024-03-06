var createError = require("http-errors");
var express = require("express");
var path = require("path");
var cookieParser = require("cookie-parser");
var logger = require("morgan");

var indexRouter = require("./routes/index");
var usersRouter = require("./routes/users");

var app = express();

// view engine setup
app.set("views", path.join(__dirname, "views"));
app.set("view engine", "ejs");

app.use(logger("dev"));
app.use(express.json()); // 用于解析 application/json
app.use(express.urlencoded({ extended: false })); // 用于解析 application/x-www-form-urlencoded
app.use(cookieParser()); // 用于解析 cookie
app.use(express.static(path.join(__dirname, "public"))); // 设置静态文件目录

app.use("/", indexRouter);

// catch 404 and forward to error handler
app.use(function (req, res, next) {
  next(createError(404));
});

// error handler
app.use(function (err, req, res, next) {
  // set locals, only providing error in development
  res.locals.message = err.message;
  res.locals.error = req.app.get("env") === "development" ? err : {};

  // render the error page
  res.status(err.status || 500);
  res.render("error");
});

process.env.PORT = 8000;

// module.exports = app;
app.listen(process.env.PORT, function () {
  console.log("账单列表, 访问地址: http://localhost:8000/account");
  console.log("添加列表, 访问地址: http://localhost:8000/create");
});
