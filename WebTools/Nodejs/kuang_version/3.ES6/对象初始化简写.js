var info = {
    name: 'bayyy',
    age: 18,
    go: function () {
        console.log('go');
    }
}

// ES6
// 对象是以key:value的形式存在的
// 1. 如果key和变量名一致, 可以只定义一次
// 2. 如果value是一个函数, 可以省略function关键字, 只剩下() {}
var name = 'bayyy';
var age = 18;
let info2 = {
    name,
    age,
    go() {
        console.log('go');
    }
};
console.log(info);  // { name: 'bayyy', age: 18, go: [Function: go] }