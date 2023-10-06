const express = require("express");
const session = require("express-session");
const MongoStore = require("connect-mongo");

const app = express();

app.use(
  session({
    name: "sid", // 设置cookie的name，默认值是：connect.sid
    secret: "bayyy", // 用来对session id相关的cookie进行签名(加盐)
    saveUninitialized: false, // 是否自动保存未初始化的会话，建议false
    resave: true, // 是否每次都重新保存会话
    store: MongoStore.create({
      mongoUrl: "mongodb://localhost:27017/users", // mongodb链接地址
    }),
    cookie: {
      httpOnly: true, // 开启后前端无法通过 JS 操作cookie
      maxAge: 1000 * 60 * 60 * 24, // 设置cookie过期时间(毫秒) -> 1天
    },
  })
);

// Home
app.get("/", (req, res) => {
  res.send("<h1>HOME</h1>");
});

// Login
app.get("/login", (req, res) => {
  // 当且仅当 username=admin&password=123 时, 登录成功, 并且设置session
  if (req.query.username === "admin" && req.query.password === "123") {
    // 设置session信息
    req.session.username = "admin";
    req.session.uid = "131";
    res.send("<h1>登录成功</h1>");
  } else {
    res.send("<h1>登录失败</h1>");
  }
});

// session 读取
app.get("/cart", (req, res) => {
  if (req.session.username) {
    res.send("<h1>购物车</h1>");
  } else {
    res.send("<h1>请登录</h1>");
  }
});

// session 销毁
app.get("/logout", (req, res) => {
  req.session.destroy((err) => {
    if (err) {
      console.log(err);
    } else {
      res.send("<h1>退出登录</h1>");
    }
  });
});

app.listen(8000, () => {
  console.log("http://localhost:8000");
});
