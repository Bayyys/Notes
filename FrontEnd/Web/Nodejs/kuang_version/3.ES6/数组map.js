// 数组map
let arr = [1, 2, 3, 4, 5];

// 传统方式
let newArr = [];
for (let i = 1; i <= arr.length; i++) {
    newArr.push(i * 2);
}
console.log(newArr); // [2, 4, 6, 8, 10]


// ES6
let newArr2 = arr.map(item => item * 2);
console.log(newArr2); // [2, 4, 6, 8, 10]


var users = [{ age: 10, school: "小学" }, { age: 20, school: "中学" }, { age: 30, school: "大学" }];
var newUsers = users.map(item => {
    item.age = item.age + 1;
    item.check = true;
    return item;
});
console.log(newUsers);  // [ { age: 11, school: '小学', check: true }, { age: 21, school: '中学', check: true }, { age: 31, school: '大学', check: true } ]