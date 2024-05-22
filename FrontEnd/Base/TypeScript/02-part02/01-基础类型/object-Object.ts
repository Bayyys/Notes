let num: Object = 1;
// let num2: object = 1; // Error: Type '1' is not assignable to type 'object'.
let num3: {} = 1;

let obj1: object = { name: "Tom" };
let obj2: Object = { name: "Tom" };
let obj3: {} = { name: "Tom" };
// obj1.age = 18; // Error: Property 'age' does not exist on type 'object'.
// obj2.age = 18; // Error: Property 'age' does not exist on type 'Object'.
// obj3.age = 18; // Error: Property 'age' does not exist on type '{}'.
