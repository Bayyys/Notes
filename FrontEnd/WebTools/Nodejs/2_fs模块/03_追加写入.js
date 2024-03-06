const fs = require("fs");

fs.appendFileSync("./test.txt", `hello world! ${i}\n`, "utf8");

console.log("后续代码...");
