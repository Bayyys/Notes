//1、导入模块
const fs = require('fs');
const { promisify } = require('util');

//2、创建async函数
async function main() {
    //读取文件
    let myreadfile = promisify(fs.readFile);
    try {
        let one = await myreadfile('./resource/1.txt');
        let two = await myreadfile('./resource/2.txt');
        let three = await myreadfile('./resource/3.txt');
        console.log(one + two + three);
    } catch (e) {
        console.log(e);
    }
}
//调用函数
main();