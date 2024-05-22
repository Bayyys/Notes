interface MyFunc {
  (a: number, b: number): number;
}

const add: MyFunc = (a, b) => a + b;
// 函数的参数名不需要与接口定义的参数名一致
const sub: MyFunc = (divisor, dividend) => divisor - dividend;
