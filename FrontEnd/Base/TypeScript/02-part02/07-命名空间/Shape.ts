export namespace Shape {
  export function square(x: number): number {
    return x * x;
  }
  export function circle(r: number): number {
    return Math.PI * r ** 2;
  }
}
