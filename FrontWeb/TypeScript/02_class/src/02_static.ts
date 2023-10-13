class MyMath {
  static PI: number = 3.1416;
  static add(...args: number[]) {
    return args.reduce((prev, curr) => prev + curr, 0);
  }
  static sub(x: number, y: number) {
    return x - y;
  }

  static mul(...args: number[]) {
    return args.reduce((prev, curr) => prev * curr, 1);
  }

  static div(x: number, y: number) {
    return x / y;
  }
}

console.log(`PI: ${MyMath.PI}`);
console.log(`add: ${MyMath.add(1, 2, 3, 4, 5)}`);
console.log(`sub: ${MyMath.sub(10, 5)}`);
console.log(`mul: ${MyMath.mul(1, 2, 3, 4, 5)}`);
console.log(`div: ${MyMath.div(10, 5)}`);
