const fs = require("fs");

const rs = fs.createReadStream("./test.txt");

rs.on("open", (chunk) => {
  console.log("可读流打开了!");
  console.log(chunk.toString());
});

rs.on("end", () => {
  console.log("读取完成!");
});
