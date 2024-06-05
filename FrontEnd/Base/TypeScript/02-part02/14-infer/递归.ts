// 递归使用示例

// 翻转数组
type numArr = [1, 2, 3, 4, 5, "last"];

type ReverArr<T extends any[]> = T extends [infer U, ...infer R]
  ? [...ReverArr<R>, U]
  : T;

type reverArr = ReverArr<numArr>; // reverArr = ["last", 5, 4, 3, 2, 1]

// 