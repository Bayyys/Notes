class Promise {
  // 构造方法
  constructor(executor) {
    // 声明构造函数
    // 添加属性
    this.PromiseState = "pending";
    this.PromiseResult = null;
    // 声明属性
    this.callback = {};
    // 保存实例对象的this值
    const self = this;
    // resolve函数
    function resolve(data) {
      if (self.PromiseState !== "pending") return;
      // 1. 修改对象的状态(promiseState)
      self.PromiseState = "fulfilled"; // resolved
      // 2. 设置对象结果值(promiseResult)
      self.PromiseResult = data;
      // 调用成功的回调函数
      setTimeout(() => {
        self.callbacks.forEach((item) => {
          item.onResolved(data);
        });
      });
    }
    // reject函数
    function reject(data) {
      if (self.PromiseState !== "pending") return;
      // 1. 修改对象的状态(promiseState)
      self.PromiseState = "rejected"; // resolved
      // 2. 设置对象结果值(promiseResult)
      self.PromiseResult = data;
      // 调用失败的回调函数
      setTimeout(() => {
        self.callbacks.forEach((item) => {
          item.onRejected(data);
        });
      });
    }
    try {
      // 同步调用 executor 执行器函数
      excutor(resolve, reject);
    } catch (e) {
      // 修改 promise 对象状态为失败
      reject(e);
    }
  }

  // 添加then方法
  then(onResolved, onRejected) {
    const self = this;
    if (typeof onRejected !== "function") {
      onRejected = (reason) => reason;
    }
    if (typeof onResolved !== "function") {
      onResolved = (value) => value;
    }
    return new Promise((resolve, reject) => {
      // 封装函数
      function callback(type) {
        try {
          let result = type(self.PromiseResult);
          if (result instanceof Promise) {
            result.then(
              (v) => {
                resolve(v);
              },
              (r) => {
                reject(r);
              }
            );
          } else {
            resolve(result);
          }
        } catch (e) {
          reject(e);
        }
      }
      // 判断  PromiseState
      if (this.PromiseState === "fulfilled") {
        setTimeout(() => {
          callback(onResolved);
        });
      }
      if (this.PromiseState === "rejected") {
        setTimeout(() => {
          callback(onRejected);
        });
      }
      if (this.PromiseState === "pending") {
        this.callback.push({
          onResolved: function () {
            callback(onResolved);
          },
          onRejected: function () {
            callback(onRejected);
          },
        });
      }
    });
  }

  // 添加catch方法
  catch(onRejected) {
    return this.then(undefined, onRejected);
  }

  // 添加 resolve 方法
  static resolve(value) {
    // 返回promise对象
    return new Promise((resolve, reject) => {
      if (value instanceof Promise) {
        value.then(
          (v) => {
            resolve(v);
          },
          (r) => {
            reject(r);
          }
        );
      } else {
        resolve(value);
      }
    });
  }

  // 添加 reject 方法
  static reject(reason) {
    return new Promise((resolve, reject) => {
      reject(reason);
    });
  }

  // 添加 all 方法
  static all(promises) {
    // 返回结果为promise对象
    return new Promise((resolve, reject) => {
      //声明变量
      let count = 0;
      let arr = [];
      //遍历
      for (let i = 0; i < promises.length; i++) {
        promises[i].then(
          (v) => {
            // 得知对象的状态是成功
            // 每个promise对象 都成功
            count++;
            // 将当前promise对象成功的结果 存入到数组中
            arr[i] = v;
            // 判断
            if (count === promises.length) {
              resolve(arr);
            } // 修改状态
          },
          (r) => {
            reject(r);
          }
        );
      }
    });
  }

  // 添加 race 方法
  static race(promises) {
    return new Promise((resolve, reject) => {
      for (let i = 0; i < promises.length; i++) {
        promises[i].then(
          (v) => {
            // 修改返回对象的状态为 『成功』
            resolve(v);
          },
          (r) => {
            // 修改返回对象的状态为 『失败』
            reject(r);
          }
        );
      }
    });
  }
}
