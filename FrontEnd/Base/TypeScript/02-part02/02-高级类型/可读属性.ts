interface Point {
  readonly x: number;
  readonly y: number;
}

let p1: Point = { x: 10, y: 20 };
// p1.x = 5; // Cannot assign to 'x' because it is a read-only property.

let arr: ReadonlyArray<number> = [1, 2, 3, 4];
// arr[0] = 10; // Index signature in type 'ReadonlyArray<number>' only permits reading.

let arr2: number[] = arr as number[]; // 使用断言重写
