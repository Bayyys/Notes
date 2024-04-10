export const PI = 3.14;
export function sum(...args: number[]) {
  return args.reduce((p, c) => p + c, 0);
}
