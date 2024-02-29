import crypto from "crypto-js";

const data = "123456";

const hmac = (txt, key) => {
  return crypto.HmacMD5(txt, key).toString();
  return crypto.HmacSHA1(txt, key).toString();
  return crypto.HmacSHA512(txt, key).toString();
};

console.log("hmac_md5 :>> ", hmac(data, "key"));
