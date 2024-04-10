const fs = require("fs");

fs.rename("./test.txt", "./newTest.txt", (err) => {
  if (err) {
    console.log("操作失败!");
    return;
  } else {
    console.log("操作成功!");
  }
});
