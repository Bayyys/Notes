let a: string = "hello";
console.log(a);

console.log("Hello TypeScript");

function fn(): void {
  return;
}

// {} 用来指定对象中可以包含哪些属性
// 语法：{属性名:属性值,属性名:属性值}
// 在属性名后面加上?，表示属性是可选的
let obj: { name: string; age?: number };
obj = { name: "张三" };

// [propName: string]: any 表示可以添加任意属性，任意属性的值可以是任意类型
let obj2: { name: string; [propName: string]: any };
obj2 = { name: "李四", sex: "男", age: 18 };

// 设置函数结构的类型声明
let funObj: (a: number, b: number) => number;
funObj = function (a: number, b: number): number {
  return a + b;
};
