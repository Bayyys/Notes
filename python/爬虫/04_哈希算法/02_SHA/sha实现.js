import crypto from "crypto-js";

const data = "123456";

const SHA1 = (txt) => {
  return crypto.SHA1(txt).toString();
};

const SHA2 = (txt) => {
  return crypto.SHA3(txt).toString();
};

const SHA3 = (txt, cnt) => {
  switch (cnt) {
    case 224:
      return crypto.SHA224(txt).toString();
    case 256:
      return crypto.SHA256(txt).toString();
    case 384:
      return crypto.SHA384(txt).toString();
    case 512:
      return crypto.SHA512(txt).toString();
  }
};

console.log("SHA1 :>> ", SHA1(data));
console.log("SHA2 :>> ", SHA2(data));
