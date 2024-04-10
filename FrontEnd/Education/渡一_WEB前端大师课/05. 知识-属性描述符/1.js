var obj = {
  b: 2,
};

// 得到属性描述符
var desc = Object.getOwnPropertyDescriptor(obj, "b");
console.log(desc); // { value: 2, writable: true, enumerable: true, configurable: true }

// 设置属性描述符
Object.defineProperty(obj, "a", {
  value: 10,
  writable: false, // 不可重写
  enumerable: false, // 不可遍历
  configurable: false, // 不可修改描述符本身
});
// Object.defineProperty(obj, 'a', {
//   writable: true,
// });  // TypeError: Cannot redefine property: a
obj.a = "abc";
console.log(obj.a); // 10 [不会被修改]

for (var key in obj) {
  console.log(key); // b [a 不会被遍历]
}

var keys = Object.keys(obj);
console.log(keys); // [ 'b' ] [a 不会被遍历]

console.log(obj); // { b: 2}
