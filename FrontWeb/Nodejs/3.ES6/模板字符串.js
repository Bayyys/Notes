// 字符串会涉及到动态部分

var name = 'bayyy';
var age = 18;

// ES6之前
var str = 'my name is ' + name + ', age is ' + age;
console.log(str);

// ES6
var str = `my name is ${name}, age is ${age}`;
console.log(str);