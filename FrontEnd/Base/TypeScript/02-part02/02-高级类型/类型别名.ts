// 定义类型别名
type str = string;
let s: str = "hello";

// 定义函数别名
type fn = () => void;
let f: fn = () => {
  console.log("func");
};

// 定义联合类型
type strOrNum = string | number;
let son1 = "hello";
let son2 = 123;

// 定义值的名义
type value = boolean | 0 | 123 | "hello";
let v1: value = true;
let v2: value = false;
let v3: value = 123;
let v4: value = "hello";
