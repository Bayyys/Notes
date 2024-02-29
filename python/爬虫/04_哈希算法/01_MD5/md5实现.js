import crypto from "crypto-js";

const data = "123456";
const md5code = crypto.MD5(data).toString();
console.log(`md5code -> {md5code}`); // md5code :>>  e10adc3949ba59abbe56e057f20f883e
console.log(`md5code.length -> ${md5code.length}`); // md5code.length -> 32
