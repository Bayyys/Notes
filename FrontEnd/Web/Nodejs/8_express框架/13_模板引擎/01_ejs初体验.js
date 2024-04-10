const fs = require("fs");
// 1. 导入 ejs
const ejs = require("ejs");

// 字符串
let china = "中国";
let str = `我爱你 ${china}`;
console.log(str); // 我爱你 中国

// 使用 ejs 渲染 -  1. 字符串
let str2 = "我爱你 <%= china %>";
let result2 = ejs.render(str2, { china: china });
console.log(result2); // 我爱你 中国

// 使用 ejs 渲染 -  2. 文件
let str3 = fs.readFileSync(__dirname + "/01_html.html").toString();
let nowTime = new Date().toLocaleString();
let result3 = ejs.render(str3, { china, nowTime });
console.log(result3); // 我爱你 中国
