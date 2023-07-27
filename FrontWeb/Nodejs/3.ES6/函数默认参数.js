// 函数默认参数

function sum(a, b) {
    return a + b;
}

var result = sum(1, 2);
console.log("计算结果是: "+result);


// ES6 默认参数
function sum(a, b = 10) {
    return a + b;
}
console.log("计算结果是: " + sum(1)); // 11