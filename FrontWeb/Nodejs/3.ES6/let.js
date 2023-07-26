// var 声明的变量没有块级作用域
// let 声明的变量有块级作用域
{
    var a = 0;
    let b = 1;
    // 定义常量
    const c = Math.PI;  // 3.141592653589793
    // let 与 const 的区别
    // 1. let 声明的变量可以修改，const 声明的变量不可以修改
    c = 3.14;  // TypeError: Assignment to constant variable.
    // 2. const 声明的变量必须初始化
    const d;  // SyntaxError: Missing initializer in const declaration
}
console.log(a); // 0
console.log(b); // ReferenceError: b is not defined

// var 声明的变量可以重复声明
// let 声明的变量不可以重复声明
var a = 0;
var a = 1;
console.log(a); // 1

let b = 0;
let b = 1;
console.log(b); // SyntaxError: Identifier 'b' has already been declared

// var 声明的变量没有变量提升
// let 声明的变量有变量提升
console.log(a); // undefined
var a = 0;

console.log(b); // ReferenceError: b is not defined
let b = 0;