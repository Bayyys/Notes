export let num = 1;
export function add(a: number, b: number): number {
  return a + b;
}

function mysub(a: number, b: number): number {
  return a - b;
}
// 导出部分重命名
export { mysub as sub };
