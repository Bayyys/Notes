class Animal {
  name: string;
  constructor(name: string) {
    this.name = name;
  }

  bark() {
    console.log("Animal bark");
  }
}

class Dog extends Animal {
  bark() {
    console.log("Woof! Woof!");
    super.bark();
  }
}

class Cat extends Animal {
  meow() {
    console.log("Meow! Meow!");
  }
}

const dog = new Dog("dog");
dog.bark();
const cat = new Cat("cat");
cat.meow();
