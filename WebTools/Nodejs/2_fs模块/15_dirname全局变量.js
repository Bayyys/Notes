const fs = require("fs");
let data = fs.readFileSync(__dirname+'/test/01.txt', 'utf-8');
console.log(data);