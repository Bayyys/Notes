interface Obj {
  name: string;
  age: number;
}
let obj = {
  name: "Tom",
  age: 25,
};
type key = keyof Obj;
const getVal = <T extends Obj, K extends keyof T>(obj: T, key: K) => {
  return obj[key];
};
