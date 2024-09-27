var o = (function () {
  var obj = {
    a: 1,
    b: 2,
  };
  // 使 obj 对象的原型指向 null, 防止原型链上的属性被访问
  Object.setPrototypeOf(obj, null);
  return {
    get: function (k) {
      // if (!obj.hasOwnProperty(k)) {
      //   return undefined;
      // }
      return obj[k];
    },
  };
})();

// 不修改代码情况下, 修改 obj 对象
// console.log(o.get("valueOf")()); // [Function: valueOf]
// const valueOf = Object.prototype.valueOf;
// valueOf();

Object.defineProperty(Object.prototype, "newThis", {
  get: function () {
    return this;
  },
});
const obj2 = o.get("newThis");
obj2.a = "change";
console.log(obj2.a); // change
console.log(o.get("a")); // change
