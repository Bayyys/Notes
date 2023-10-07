const db = require("./db/db");
// 直接进行数据库操作, 若数据库未启动, 则不进行启动
db(
  () => {
    var createError = require("http-errors");
    var express = require("express");
    var path = require("path");
    var cookieParser = require("cookie-parser");
    var logger = require("morgan");
    const session = require("express-session");
    const MongoStore = require("connect-mongo");
    const { DBHOST, DBPORT, DBNAME, port } = require("./config/config");

    const https = require("https");
    https
      .createServer(
        {
          key: fs.readFileSync("/etc/letsencrypt/path/to/privkey.pem"),
          cert: fs.readFileSync("/etc/letsencrypt/path/to/cert.pem"),
          ca: fs.readFileSync("/etc/letsencrypt/path/to/chain.pem"),
        },
        app
      )
      .listen(443, () => {
        console.log("HTTPS Server is running on: https://localhost:%s", 443);
      });

    const indexRouter = require("./routes/web/index");
    const regRouter = require("./routes/web/auth");
    const authApiRouter = require("./routes/api/auth");
    const accountRouter = require("./routes/api/account");

    var app = express();

    // view engine setup
    app.set("views", path.join(__dirname, "views"));
    app.set("view engine", "ejs");

    app.use(logger("dev"));
    app.use(express.json()); // 用于解析 application/json
    app.use(express.urlencoded({ extended: false })); // 用于解析 application/x-www-form-urlencoded
    app.use(cookieParser()); // 用于解析 cookie
    app.use(express.static(path.join(__dirname, "public"))); // 设置静态文件目录

    app.use(
      session({
        name: "sid", // 设置cookie的name，默认值是：connect.sid
        secret: "bayyy", // 用来对session id相关的cookie进行签名(加盐)
        saveUninitialized: false, // 是否自动保存未初始化的会话，建议false
        resave: true, // 是否每次都重新保存会话
        store: MongoStore.create({
          mongoUrl: `mongodb://${DBHOST}:${DBPORT}/${DBNAME}`, // mongodb链接地址
        }),
        cookie: {
          httpOnly: true, // 开启后前端无法通过 JS 操作cookie
          maxAge: 1000 * 60 * 60 * 24, // 设置cookie过期时间(毫秒) -> 1天
        },
      })
    );

    app.use("/", indexRouter);
    app.use("/", regRouter);
    app.use("/api", accountRouter);
    app.use("/api", authApiRouter);

    // catch 404 and forward to error handler
    app.use(function (req, res, next) {
      // 响应404页面
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

    process.env.PORT = port;

    // module.exports = app;
    app.listen(process.env.PORT, function () {
      console.log(
        `账单列表, 访问地址: http://localhost:${process.env.PORT}/account`
      );
      console.log(
        `添加列表, 访问地址: http://localhost:${process.env.PORT}/create`
      );
      console.log(
        `注册列表, 访问地址: http://localhost:${process.env.PORT}/reg`
      );
      console.log(
        `登录列表, 访问地址: http://localhost:${process.env.PORT}/login`
      );
    });
  },
  () => {}
);
