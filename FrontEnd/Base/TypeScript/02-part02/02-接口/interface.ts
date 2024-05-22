interface Person {
  name: string;
  sex?: boolean;
  age?: number;
  sayHello(): void;
}

let tom: Person = {
  name: "Tom",
  sex: true,
  sayHello() {
    console.log("hello!");
  },
};
