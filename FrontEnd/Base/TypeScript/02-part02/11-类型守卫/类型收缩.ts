// 类型收缩
// 1. if 判断 typeof
const isString = (val) => typeof val === "string";
const whatType = (val: string | number | boolean) => {
  switch (typeof val) {
    case "string":
      return "string";
    case "number":
      return "number";
    case "boolean":
      return "boolean";
    default:
      throw new Error("unsupported type");
  }
};

// 2. instanceof
const isDate = (val) => val instanceof Date;
const isArray = (val) => Array.isArray(val);

// 3. in
class A {
  a: number = 1;
}
class B {
  b: string = "b";
}
const isA = (val: A | B) => "a" in val;
