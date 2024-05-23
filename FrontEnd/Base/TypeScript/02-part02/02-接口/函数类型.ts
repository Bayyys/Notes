interface MyFunc {
  (a: number, b: number): number;
}

const add: MyFunc = (a, b) => a + b;
// 函数的参数名不需要与接口定义的参数名一致
const sub: MyFunc = (divisor, dividend) => divisor - dividend;

const mul = (a: number, b: number): number => a * b;

// 可选参数
const mod = (a: number, b?: number): number => (b ? a % b : a);

// 默认参数
const div = (a: number = 1, b: number = 1): number => a / b;

// this 类型: 用于限制函数中的 this 对象
// this 定义在函数参数列表的最前面
// 使用时忽略 this 参数
interface Obj {
  name: string;
  getName(): string;
  sayHello: (this: Obj, msg: string) => void;
}

let obj: Obj = {
  name: "张三",
  getName() {
    return this.name;
  },
  sayHello(this, msg) {
    console.log(`${this.name} say: ${msg}`);
  },
};

// 剩余参数
const sum = (a: number, b: number, ...rest: number[]): number => {
  return rest.reduce((prev, curr) => prev + curr, a + b);
};

// 函数重载
let arr = [1, 2, 3];
function findArray(id: number): number[];
function findArray(id: number[]): number[];
function findArray(): number[];
function findArray(ids?: number | number[]): number[] {
  if (typeof ids === "number") {
    return arr.filter((item) => item === ids);
  } else if (Array.isArray(ids)) {
    return [...arr, ...ids];
  } else {
    return arr;
  }
}
console.log(findArray([4, 5, 6]));
