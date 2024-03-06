const fs = require("fs");

fs.stat("./test/01.txt", (err, stats) => {
  if (err) {
    console.log("获取文件信息失败!");
    return;
  } else {
    console.log(stats);
    console.log(stats.isFile());
    console.log(stats.isDirectory());
  }
});