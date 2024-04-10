const fs = require("fs");

const ws = fs.createWriteStream("./test.txt", { flags: 'a'});

if (ws.writable) {
  ws.write("11111111111111");
  if (ws.write("写入文件内容")) {
    console.log("写入成功!");
  }
}

ws.close();