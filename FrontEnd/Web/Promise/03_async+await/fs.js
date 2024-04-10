const fs = require("fs");
const util = require("util");
const myReadFile = util.promisify(fs.readFile);

// 回调函数形式
// fs.readFile("./resources/1.txt", (err, data) => {
//   if (err) throw err;
//   fs.readFile("./resources/2.txt", (err, data2) => {
//     if (err) throw err;
//     fs.readFile("./resources/3.txt", (err, data3) => {
//       let result = data + "\r\n" + data2 + "\r\n" + data3;
//       console.log(result);
//     });
//   });
// });

// async await形式
async function main() {
  try {
    let data1 = await myReadFile("./resources/1.txt");
    let data2 = await myReadFile("./resources/2.txt");
    let data3 = await myReadFile("./resources/3.txt");
    let result = data1 + "\r\n" + data2 + "\r\n" + data3;
    console.log(result);
  } catch (e) {
    console.log(e);
  }
}
main();
