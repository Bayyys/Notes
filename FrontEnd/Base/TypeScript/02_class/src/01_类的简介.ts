class Person {
  private count: number = 0; // private: 只能在类内部访问
  name: string;
  private _age: number;
  static type: string = "人类"; // static: 静态属性，可以通过类名直接访问

  constructor(name: string, age: number) {
    this.name = name;
    this._age = age;
    this.count++;
  }

  sayHello() {
    console.log(`Hello, ${this.name}`);
  }

  get age() {
    return this._age;
  }

  set age(age: number) {
    if (age < 0) {
      throw new Error("年龄不能为负数");
    }
    this._age = age;
  }

  get getCount() {
    return this.count;
  }
}

console.log(`Person.type: ${Person.type}`);
const p = new Person("张三", 18);
console.log(`name: ${p.name}, age: ${p.age}, type: ${Person.type}`);
console.log("一年过去后....");
p.age++;
console.log(`name: ${p.name}, age: ${p.age}, type: ${Person.type}`);
