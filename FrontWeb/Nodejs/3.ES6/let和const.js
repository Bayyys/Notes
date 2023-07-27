// let 和 const
// 1. var 的变量穿透问题
// 2. 常量修改问题
// 3. 初始化问题


for (var i = 0; i < 5; i++) {
    console.log(i);
}
console.log(i); // 5

for (let i = 0; i < 5; i++) {
    console.log(i);
}
console.log(i); // 报错

let a = 1;
a = 2;  // 可以修改

const b = 1;
b = 2;  // 报错