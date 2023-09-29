const fs = require("fs");

try {
  fs.writeFileSync("test.txt", "Hello World!");
  console.log("文件写入成功!");
} catch (e) {
  console.log(e);
}

console.log("后续代码...");
