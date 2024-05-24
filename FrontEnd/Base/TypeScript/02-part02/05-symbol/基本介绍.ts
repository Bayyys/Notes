let a1: symbol = Symbol(1); // 唯一的值
let a2: symbol = Symbol(1);
console.log(a1 === a2); // false

console.log(Symbol.for("foo") === Symbol.for("foo")); // true

let obj = {
  name: "jack",
  [a1]: "a1",
  [a2]: "a2",
};

// 仅能读取到字符串键
for (const key in obj) {
  console.log(key); // name
}
console.log(Object.keys(obj)); // ["name"]
console.log(Object.getOwnPropertyNames(obj)); // ["name"]

// 仅能读取到 Symbol 键
console.log(Object.getOwnPropertySymbols(obj)); // [Symbol(1), Symbol(1)]

// 读取所有键
console.log(Reflect.ownKeys(obj)); // ["name", Symbol(1), Symbol(1)]
