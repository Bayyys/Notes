const fs = require("fs");

console.log("当前文件的绝对路径:", __dirname);

fs.rmdir("./test", { recursive: true }, (err) => {
  if (err) {
    console.log("删除失败!");
    return;
  } else {
    console.log("删除成功!");
  }
});

fs.readdir("./", (err, files) => {
  if (err) {
    console.log("读取失败!");
    return;
  } else {
    console.log(files);
  }
});

// 1. 简单创建
fs.mkdir("./test", (err) => {
  if (err) {
    console.log("创建失败!");
    return;
  } else {
    console.log("创建成功!");
  }
});

// 2. 递归创建
fs.mkdir("./test/test1/test2", { recursive: true }, (err) => {
  if (err) {
    console.log("创建失败!");
    return;
  } else {
    console.log("创建成功!");
  }
});
