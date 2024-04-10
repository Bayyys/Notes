// 导入 jwt
const jwt = require("jsonwebtoken");

// 创建(生成) token
// let token = jwt.sign(用户数据, 加密字符串, 配置对象);
const token = jwt.sign(
  {
    username: "zhangsan",
  },
  "bayyy",
  {
    expiresIn: 3, // 过期时间(单位: 秒)
  }
);

// 校验 token
jwt.verify(token, "bayyy", (err, data) => {
  if (err) {
    console.log(err);
  }
  console.log(data);
});
