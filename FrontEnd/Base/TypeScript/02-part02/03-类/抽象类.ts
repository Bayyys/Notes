abstract class Animal {
  name: string;
  constructor(name: string) {
    this.name = name;
  }
  abstract makeSound(): void;
  move(): void {
    console.log("roaming the earth...");
  }
}

class Dog extends Animal {
  constructor(name: string) {
    super(name);
  }
  makeSound(): void {
    console.log("Woof! Woof!");
  }
}

let dog = new Dog("旺财");
dog.makeSound();
dog.move();
