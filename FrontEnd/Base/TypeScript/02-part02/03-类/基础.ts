interface PersonInfo {
  name: string;
  age: number;
  sex?: boolean;
}

interface PersonCls {
  info: PersonInfo;
  sayHello(msg: string): void;
}

class School {
  schoolName: string;
  address?: string;
  constructor(schoolName: string = "清华大学", address?: string) {
    this.schoolName = schoolName;
    this.address = address;
  }
}

class Student extends School implements PersonCls {
  info: PersonInfo;

  constructor(
    info: PersonInfo,
    schoolName: string = "清华大学",
    address?: string
  ) {
    super(schoolName, address);
    this.info = info;
  }
  sayHello(msg: string): void {
    console.log(`${this.info.name} which in ${this.schoolName} say: ${msg}`);
  }
}

let zhangsan = new Student({ name: "张三", age: 18 });
zhangsan.sayHello("Hello World!");
