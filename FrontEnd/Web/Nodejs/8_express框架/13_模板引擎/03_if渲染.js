let isLogin = true;

const ejs = require("ejs");
const fs = require("fs");

let result1 = ejs.render(
  `<% if(isLogin) { %>
    <a href="#">退出</a>
  <% } else { %>
    <button>登录</button>
    <button>注册</button>
  <% } %>`,
  { isLogin }
);

const str = fs.readFileSync(__dirname + "/03_if渲染.html").toString();
const result2 = ejs.render(str, { isLogin });

console.log(result1);
console.log(result2);
