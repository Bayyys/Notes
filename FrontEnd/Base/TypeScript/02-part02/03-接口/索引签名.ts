interface Point {
  readonly x: number;
  readonly y: number;
  [propName: string]: any;
}

let p2: Point = { x: 10, y: 20, use: "type" };
p2.dimension = 3;
