const fs = require("fs");

const files = fs.readdirSync("./test");

files.forEach((item, index) => {
  const [name, txt] = item;
  const num = index
  if (Number(num) < 10) {
    fs.rename(`./test/${item}`, `./test/0${num}.txt`, (err) => {});
  } else {
    fs.rename(`./test/${item}`, `./test/${num}.txt`, (err) => {});
  }
});
