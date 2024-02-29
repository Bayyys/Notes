// 浏览器方法
// window.btoa("123"); // 编码
// window.atob("MTIz"); // 解码

// Node.js方法
const str = "123";
const code = Buffer.from(str, "utf-8").toString("base64");
console.log("code :>> ", code);

const encode = Buffer.from(code, "base64").toString("utf-8");
console.log("encode :>> ", encode);
