var createError = require('http-errors'); // 错误处理模块(http-errors)
var express = require('express');
var path = require('path');
var cookieParser = require('cookie-parser');  // cookie解析中间件(cookie-parser)
var logger = require('morgan'); // 日志中间件(morgan)

var indexRouter = require('./routes/index');  // 路由
var usersRouter = require('./routes/users');  // 路由

var app = express();

// 设置模板引擎
app.set('views', path.join(__dirname, 'views'));  // 模板文件存放的目录
app.set('view engine', 'ejs');  // 模板引擎

app.use(logger('dev')); // 用来记录日志的
app.use(express.json());  // 用来解析json格式的请求体
app.use(express.urlencoded({ extended: false })); // 用来解析urlencoded格式的请求体
app.use(cookieParser());  // 用来解析cookie
app.use(express.static(path.join(__dirname, 'public')));  // 静态文件服务

app.use('/', indexRouter);
app.use('/users', usersRouter);

// 捕获404错误并转发到错误处理器
app.use(function(req, res, next) {
  next(createError(404));
});

// 错误处理器
app.use(function(err, req, res, next) {
  // 设置本地变量，只提供开发中的错误
  res.locals.message = err.message; // 错误信息
  res.locals.error = req.app.get('env') === 'development' ? err : {}; // 错误对象

  // 渲染错误页面
  res.status(err.status || 500);  // 设置状态码
  res.render('error');  // 渲染模板
});

module.exports = app;
