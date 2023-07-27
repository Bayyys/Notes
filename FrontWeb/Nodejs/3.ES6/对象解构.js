// 对象解构
let info = {
    name: 'bayyy',
    age: 18,
    go: function () {
        console.log('go');
    }
};

// 获取对象中的属性值
// 1. 通过.的方式获取
console.log(info.name); // bayyy
// 2. 通过[]的方式获取
console.log(info['name']); // bayyy

// ES6
// 对象解构: 快速获取属性和方法的一种形式
var { name, age, go } = info;
go(); // go


// 为什么对象取值要提供两种方式?
// 1. 如果属性名是一个变量, 那么就只能通过[]的方式获取(即属性名和已经定义的变量名不一致)
// 2. 如果属性名是一个字符串, 那么就可以通过.和[]的方式获取