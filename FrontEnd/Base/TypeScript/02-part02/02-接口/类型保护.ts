// typeof
const myToString = (arg: number | string): string => {
  if (typeof arg === "number") {
    return arg.toString();
  } else if (typeof arg === "string") {
    return arg;
  } else {
    return "Error Input";
  }
};

// instanceof
class Obj1 {
  name: string;
  age: number;
}
class Obj2 {
  id: number;
  sex: boolean;
}
const myToNumber = (arg: Obj1 | Obj2): void => {
  if (arg instanceof Obj1) {
    console.log(arg.name);
  } else if (arg instanceof Obj2) {
    console.log(arg.id);
  }
};
