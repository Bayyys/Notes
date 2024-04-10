const fs = require("fs");

fs.readFile("./test.txt", "utf8", (err, data) => {
  if (err) {
    console.log("读取文件失败!");
    return;
  }
  console.log(data);
});
