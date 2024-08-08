/**
 * 手写 call 方法
 * 不得使用 apply、bind 辅助
 */

Function.prototype.myCall = function (ctx, ...args) {
  ctx = ctx || globalThis;
  const key = Symbol();
  Object.defineProperty(ctx, key, {
    value: this,
    enumerable: false,
  });
  ctx[key] = this;
  const res = ctx[key](...args);
  delete ctx.fn;
  return res;
};

function method(a, b) {
  console.log(this, a, b);
  return a + b;
}

method.myCall({}, 1, 2); // { name: 'call' } 1 2
