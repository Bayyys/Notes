const fs = require("fs");

// 回调函数形式
fs.readFile("./resource/content.txt", (err, data) => {
  if (err) throw err;
  console.log("------------回调函数形式------------");
  console.log(data.toString());
});

// Promise形式
let p = new Promise((resolve, reject) => {
  fs.readFile("./resource/content.txt", (err, data) => {
    if (err) reject(err);
    resolve(data);
  });
}).then(
  (value) => {
    console.log("------------Promise形式------------");
    console.log(value.toString());
  },
  (reason) => {
    console.log(reason);
  }
);
