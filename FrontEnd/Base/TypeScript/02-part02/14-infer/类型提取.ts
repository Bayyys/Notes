// 提取头部元素
type Arr = ["1", "2", "3"];
type First<T> = T extends [infer U, ...any[]] ? U : never;

type head = First<Arr>; // head = "1"

// 提取尾部元素
type Last<T extends any[]> = T extends [...any[], infer U] ? U : never;

type tail = Last<Arr>; // tail = "3"

//  剔除尾部元素
type Pop<T extends any[]> = T extends [...infer U, any] ? U : never;
type popArr = Pop<Arr>; // popArr = ["1", "2"]

// 剔除头部元素
type Shift<T extends any[]> = T extends [any, ...infer U] ? U : never;
type shiftArr = Shift<Arr>; // shiftArr = ["2", "3"]
