const fs = require("fs");

// unlink/unlinkSync
fs.unlink("./test2.txt", (err) => {
  if (err) {
    console.log("删除失败!");
    return;
  } else {
    console.log("删除成功!");
  }
});

// rm/rmSync
fs.rm("./test3.txt", (err) => {
  if (err) {
    console.log("删除失败!");
    return;
  } else {
    console.log("删除成功!");
  }
});
