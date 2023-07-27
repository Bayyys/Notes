// 箭头函数(重点): 小程序, uni-app, vue, 常见脚手架大量使用

var sum = function(a, b) {
    return a + b;
}

// 箭头函数-改进1: 去掉function关键字, 加上箭头
var sum = (a, b) => {
    return a + b;
}

// 箭头函数-改进2: 如果函数体只有一行代码, 可以省略{}
var sum = (a, b) => a + b;

// 应用
var arr = [1, 2, 3, 4, 5];

var newArr = arr.map(function (item) {
    return item * 2;
}); // [2, 4, 6, 8, 10]

// 使用箭头函数
var newArr = arr.map(item => item * 2);