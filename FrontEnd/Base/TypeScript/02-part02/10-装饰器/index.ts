// 1. 类装饰器 ClassDecorator
// const classDecoratorFunc: ClassDecorator = (classConstructor: Function) => {
//   console.log("run classDecoratorFunc");
//   console.log(classConstructor); // [class MyClass]
//   classConstructor.prototype.newProp = "newProp";
//   classConstructor.prototype.sayHello = function () {
//     console.log("hello world");
//   };
// };

// @classDecoratorFunc
// class MyClass {
//   hello: string;
//   constructor(m: string) {
//     console.log("run constructor");
//     this.hello = m;
//   }
// }
// const myClassInstance = new MyClass("world") as any;
// myClassInstance.sayHello();
// console.log(myClassInstance.newProp); // newProp

// 2. 属性装饰器 PropertyDecorator
import "reflect-metadata";

const formatMetadataKey = Symbol("format");
const myformat = (formatString: string): PropertyDecorator => {
  return (target, propertyKey) => {
    console.log("🚀 ~ reutrn ~ target:", target); // 类的原始对象 {}
    console.log("🚀 ~ reutrn ~ propertyKey:", propertyKey); // 成员名 name
    Reflect.metadata(formatMetadataKey, formatString)(target, propertyKey);
  };
};
const getFormat = (target: any, propertyKey: string) => {
  return Reflect.getMetadata(formatMetadataKey, target, propertyKey);
};
class PropertyDecoratorClass {
  @myformat("name: %s")
  name: string = "bayyy";
  showname() {
    console.log(getFormat(this, "name"), this.name);
  }
}
new PropertyDecoratorClass().showname(); // name: bayyy

// 3. 参数装饰器 ParameterDecorator
// import "reflect-metadata";

// const showExtraInfo = (): MethodDecorator => {
//   return (target, _, descriptor) => {
//     const key = Reflect.getMetadata("extraInfo", target);
//     (descriptor.value as Function)(key ? "has extraInfo" : "no extraInfo");
//   };
// };

// const addExtraInfo = (): ParameterDecorator => {
//   return (target, propertyKey, parameterIndex) => {
//     console.log("🚀 ~ return ~ target:", target); // 类的原型对象 {}
//     console.log("🚀 ~ return ~ propertyKey:", propertyKey); // 成员名 sayHello
//     console.log("🚀 ~ return ~ parameterIndex:", parameterIndex); // 参数在函数列表中的索引 0
//     Reflect.defineMetadata("extraInfo", "extraInfo", target);
//   };
// };

// class ParameterDecoratorClass {
//   @showExtraInfo()
//   sayHello(@addExtraInfo() name: string) {
//     console.log(name);
//   }
// }

// 4. 方法装饰器 MethodDecorator
// // 4.1 普通方法装饰器
// const methodDecoratorFunc: MethodDecorator = (
//   target, // 静态成员->类的构造函数，实例成员->类的原型对象
//   propertyKey, // 方法名
//   descriptor // 属性描述符
// ) => {
//   console.log("run methodDecoratorFunc");
//   console.log(target); // {}
//   console.log(propertyKey); // sayHello
//   console.log(descriptor); // { value: [Function: sayHello], writable: true, enumerable: false, configurable: true }
// };

// // 4.2 装饰器工厂
// const methodDecoratorFactory = (param: string): MethodDecorator => {
//   return (
//     target, // 静态成员->类的构造函数，实例成员->类的原型对象
//     propertyKey, // 方法名
//     descriptor // 属性描述符
//   ) => {
//     console.log("run methodDecoratorFunc");
//     console.log(target); // {}
//     console.log(propertyKey); // sayHello
//     console.log(descriptor); // { value: [Function: sayHello], writable: true, enumerable: false, configurable: true }
//   };
// };

// class MethodDecoratorClass {
//   @methodDecoratorFactory("param")
//   sayHello() {
//     console.log("hello world");
//   }
// }

// 5. 装饰器工厂 DecoratorFactory [函数柯里化]
// function decoratorFactoryFunc(param: string): ClassDecorator {
//   return (classConstructor: Function) => {
//     console.log("run decoratorFactoryFunc");
//     console.log(classConstructor);
//     classConstructor.prototype.newProp = param;
//   };
// }

// @decoratorFactoryFunc("param")
// class ClassFactory {
//   hello: string;
//   constructor(m: string) {
//     console.log("run constructor");
//     this.hello = m;
//   }
// }
// const factoryInstance = new ClassFactory("world") as any;
// console.log(factoryInstance.newProp); // param
