/**
 * 手写 Promise.all 函数
 */
Promise.myAll = function (proms) {
  let res, rej;
  const p = new Promise((resolve, reject) => {
    res = resolve;
    rej = reject;
  });
  // 设置 p 的状态
  const result = [];
  let count = 0;
  let fulFilled = 0; // 记录已经完成的 promise 数量
  for (const prom of proms) {
    const i = count;
    count++;
    Promise.resolve(prom).then((data) => {
      // 将数据存入 result
      result[i] = data;
      // 判断是否全部完成
      fulFilled++;
      if (fulFilled === count) {
        res(result);
      }
    }, rej);
  }
  if (count === 0) {
    res(result);
  }
  return p;
};

// Promise.all 方法解释
// 1. 接收一个 promise 数组
// 2. 返回一个新的 promise
// 3. 当所有的 promise 都 resolve 时，新 promise resolve
// 4. 当有一个 promise reject 时，新 promise reject
// 5. 返回的 promise 的 resolve 值是所有 promise 的 resolve 值组成的数组
Promise.myAll([]).then((res) => {
  console.log(res);
});
