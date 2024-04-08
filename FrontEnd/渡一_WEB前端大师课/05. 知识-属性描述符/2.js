var obj = {};

Object.defineProperty(obj, 'a', {
  get: function () {
    return 123;
  }, // 读取器 getter
  set: function (val) {
    throw new Error(
      `兄弟，你正在给a这个属性重新赋值，你所赋的值是${val}，但是，这个属性是不能复制，你再考虑考虑`
    );
  }, // 设置器 setter
});

console.log(obj.a);
obj.a = 'abx';
// console.log(obj.a); // console.log(get())
