const jwt = require("jsonwebtoken");
const { secret } = require("../config/config");

module.exports = (req, res, next) => {
  let token = req.get("token");
  if (!token) {
    return res.json({
      code: "2003",
      msg: "token 缺失, 请先登录",
      data: null,
    });
  }
  jwt.verify(token, secret, (err, data) => {
    if (err) {
      return res.json({
        code: "2004",
        msg: "登录已过期，请重新登录",
        data: null,
      });
    } else {
      req.user = data;
      next();
    }
  });
};
