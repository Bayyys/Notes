export { add } from "./math.js";
export function sum(...args) {
  return args.reduce((p, c) => p + c, 0);
}
