// 定义方法
let arr1: number[] = [1, 2, 3];
let arr2: Array<number> = [1, 2, 3];

// 接口定义数组
interface MyArray {
  name: string;
  age?: number;
  sex?: boolean;
}

let arr3: MyArray[] = [
  { name: "张三" },
  { name: "李四", age: 18 },
  { name: "王五", sex: true },
];

// 二维数组
let arr4: number[][] = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
];
let arr5: Array<Array<string>> = [
  ["one", "two", "three"],
  ["four", "five", "six"],
  ["seven", "eight", "nine"],
];

// 混合类型
let arr6: (string | number)[] = ["one", 2, "three", 4];
let arr7: Array<string | number> = ["one", 2, "three", 4];
let arr8: any[] = ["one", 2, "three", 4, true];
let arr9: [number, string, boolean, {}] = [1, "two", true, {}];
