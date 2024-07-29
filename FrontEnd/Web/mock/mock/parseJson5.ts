const fs = require("fs");
const path = require("path");
const json5 = require("json5");

const json = fs.readFileSync(path.join(__dirname, "userInfo.json5"), "utf-8");
const obj = json5.parse(json);
console.log("🚀 ~ obj:", obj);
