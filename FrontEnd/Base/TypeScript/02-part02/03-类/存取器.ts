class Car {
  protected engine: string;
  constructor(engine: string) {
    this.engine = engine;
  }
  get Engine(): string {
    return this.engine;
  }
  set Engine(engine: string) {
    this.engine = engine;
  }
}
let car = new Car("V8");
console.log(car.Engine); // V8
car.Engine = "V12";
// console.log(car.engine); // error: Property 'engine' is protected and only accessible within class 'Car' and its subclasses.
