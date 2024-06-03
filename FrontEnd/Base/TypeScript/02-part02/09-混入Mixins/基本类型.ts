interface A {
  name: string;
}
interface B {
  age: number;
}
let a: A = {
  name: "a",
};
let b: B = {
  age: 10,
};

// 1. 扩展运算符 (浅拷贝)
let ab = { ...a, ...b };

// 2. Object.assign (浅拷贝) [ES6]
let ab2 = Object.assign({}, a, b);

// 3. structureClone (深拷贝) [ES6]
let a2 = structuredClone(a);
