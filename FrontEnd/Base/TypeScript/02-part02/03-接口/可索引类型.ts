interface StringArray {
  [index: number]: string;
}

let myArray: StringArray = ["Bob", "Fred"];
myArray[0] = "Alice";

interface NumberDictionary {
  [index: string]: number;
  [index: number]: number;
  length: number; // 可以，length是number类型
}
