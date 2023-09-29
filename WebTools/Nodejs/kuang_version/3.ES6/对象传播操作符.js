// 对象传播操作符
var obj = {
    name: 'bayyy',
    age: 18,
    phone: '123456789',
    go() {
        console.log('go');
    }
}

// ES6
// 解构: 对象传播操作符-将对象中剩下的属性和方法, 以一个新的对象的形式返回
var { name, age, ...other } = obj;
console.log(name);  // bayyy
console.log(age);   // 18
console.log(other); // { phone: '123456789', go: [Function: go] }

// 应用场景
// 后台返回数据 var userPage = {pages:10, users:[{},{}], pageNo:1, pageSize:10, total:100}
// var {users, ...pageInfo} = userPage;