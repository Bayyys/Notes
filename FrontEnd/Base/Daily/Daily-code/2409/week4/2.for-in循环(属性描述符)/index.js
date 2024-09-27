var obj = { a: 1, b: 2 };

Object.prototype.c = 3;

for (var key in obj) {
  console.log(key); // a, b, c
}

// 添加在原型链上的何种属性会被 for-in 循环遍历到？
var desc = Object.getOwnPropertyDescriptor(Object.prototype, "c");
console.log(desc); // { value: 3, writable: true, enumerable: true, configurable: true }

// writable: 可以修改属性的值
// enumerable: 可以被遍历
// configurable: 可以修改属性的描述符

Object.defineProperty(Object.prototype, "d", {
  value: 4,
  writable: true,
  enumerable: false,
  configurable: true,
});

for (var key in obj) {
  console.log(key); // a, b, c
}
