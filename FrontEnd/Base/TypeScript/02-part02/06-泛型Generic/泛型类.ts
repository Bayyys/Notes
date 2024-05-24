class Test<T> {
  value: T;
  constructor(value: T) {
    this.value = value;
  }
  print: (x: T, y: T) => void = (x, y) => {
    console.log(`${x} & ${y}`);
  };
}

let test = new Test<number>(123);
test.print(123, 456);
