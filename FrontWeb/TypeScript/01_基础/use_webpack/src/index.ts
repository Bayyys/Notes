function sum(...args: number[]) {
  return args.reduce((p, c) => p + c, 0);
}
console.log("Hello TypeScript!");
console.log(sum(1, 2, 3, 4, 5, 6, 7));
