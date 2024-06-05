interface Parent {
  name: string;
  age: number;
}

interface Child {
  name: string;
  age: number;
  grade: number;
}

let p: Parent = { name: "Tom", age: 25 };
let c: Child = { name: "Tom", age: 25, grade: 99 };
p = c; // Success, 子类型可以赋值给父类型 -> 协变

type handler = (child: Child) => void;

const childHandler: handler = (c: Child) => {};
const parentHandler: handler = (p: Parent) => {}; // Success, 父类型可以赋值给子类型 -> 逆变
