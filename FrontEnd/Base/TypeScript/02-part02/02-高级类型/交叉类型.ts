// 交叉类型
interface Person {
  name: string;
  sex: boolean;
  age?: number;
}

interface Student {
  stuId: number;
}

let student: Person & Student = {
  name: "张三",
  sex: true,
  // age: 18,
  stuId: 1001,
};

// 联合类型
const getLength = (content: string | string[]): number => {
  if (typeof content === "string") {
    return content.length;
  } else {
    return content.reduce((prev, curr) => prev + curr.length, 0);
  }
};
console.log(getLength("one")); // 3
console.log(getLength(["one", "two", "three"])); // 11
