let str: string = "bayyy";
let str2 = `${str}`;

console.log("🚀 ~ str:", str);
console.log("🚀 ~ str2:", str2);

let x: any = "hello";
x = 42;
x(1); // No error
x.foo = "world"; // No error
