//1、导入模块
const fs = require('fs');
const util = require('util');
//2、调用方法
const myreadFile = util.promisify(fs.readFile);
//3、读取文件
let one = myreadFile('./resource/1.txt');
let two = myreadFile('./resource/2.txt');
let three = myreadFile('./resource/3.txt');
let result = Promise.all([one, two, three]);
result.then(value => {
    console.log(value.toString());
}, reason => {
    console.log(reason);
})