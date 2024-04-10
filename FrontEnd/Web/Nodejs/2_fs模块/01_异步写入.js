// 1. 导入 fs 模块
const fs = require("fs");

// 2. 调用 fs.writeFile() 方法写入文件
// fs.writeFile(file, data[, options], callback)
//    fiel: 要写入的文件路径
//    data: 要写入的数据
//    options: 选项，可以对写入进行一些设置
//    callback: 回调函数，写入完成后执行

fs.writeFile("./test.txt", "Hello world!", (err) => {
  if (err) {
    console.log("写入失败！");
  } else {
    console.log("写入成功！");
  }
});

setTimeout(() => {
  console.log("程序执行完毕2！");
}, 2000);

console.log("程序执行完毕1！");