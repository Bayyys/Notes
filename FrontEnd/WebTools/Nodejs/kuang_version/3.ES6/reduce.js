// reduce
// 语法: arr.reduce(callback, [initialValue])
// callback: 回调函数, 有四个参数:
//      1. previousValue: 上一次调用回调返回的值, 或者是提供的初始值(initialValue)
//      2. currentValue: 数组中当前被处理的元素
//      3. index: 当前元素在数组中的索引
//      4. array: 调用reduce的数组
// initialValue: 作为第一次调用 callback函数时的第一个参数的值, 如果没有提供初始值, 则使用数组中的第一个元素
// 返回值: 函数累计处理的结果
let arr = [1, 2, 3, 4, 5];
var result = arr.reduce((prev, next) => {
    console.log(prev, next);    // prec: 上一次的返回值, next: 当前值
    return prev + next;
});
console.log(result); // 15


let arr2 = [10, 20, 30, 40, 50];
var result2 = arr2.reduce((prev, next, index, array) => {
    console.log(prev, next, index, array);
    return prev + next;
}, 100);