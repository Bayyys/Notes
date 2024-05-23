class Person {
  name: string;
  public age: number;
  protected sex?: boolean;
  private weight: number;
  constructor(name, age, sex, weight) {
    this.name = name;
    this.age = age;
    this.sex = sex;
    this.weight = weight;
  }
}

let p = new Person("张三", 18, true, 65);
p.name = "李四";
p.age = 19;
// p.sex = true; // Error: Property "sex" is protected and only accessible within class "Person" and its subclasses.
// p.weight = 65; // Error: Property "weight" is private and only accessible within class "Person".

class Teacher extends Person {
  constructor(name, age, sex, weight) {
    super(name, age, sex, weight);
    // this.weight = 70; // Error: Property "weight" is private and only accessible within class "Person".
  }
}
