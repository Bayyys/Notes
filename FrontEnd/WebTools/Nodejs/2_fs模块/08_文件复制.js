const fs = require("fs");

let data = fs.readFileSync("./test.txt", "utf8");
fs.writeFileSync("./test2.txt", data);
console.log("同步文件复制完成!")

const rs = fs.createReadStream("./test.txt");
const ws = fs.createWriteStream("./test3.txt");

rs.on("data", (chunk) => {
  ws.write(chunk)
})
console.log("异步文件复制完成!")