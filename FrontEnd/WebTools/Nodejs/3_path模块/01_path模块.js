//导入 fs
const fs = require("fs");
const path = require("path");

//resolve：拼接规范（分隔符统一）的绝对路径
console.log(path.resolve(__dirname, './index.html'));
//可以不写./也表示绝对路径
console.log(path.resolve(__dirname, 'index.html'));

//sep：获取操作系统的路径分隔符
console.log(path.sep); // windows下是\，Linux下是/

//parse解析路径并返回对象
//console.log(__filename); //获取文件的绝对路径
let str = "d:\\Coding\\test\\tempWebToolsNodejs\\3_path模块\\index.html ";
console.log(path.parse(str));

//basename：快速获取文件名
console.log(path.basename(str));

//dirname：获取路径的目录名
console.log(path.dirname(str));

//extname：获取路径的扩展名
console.log(path.extname(str));