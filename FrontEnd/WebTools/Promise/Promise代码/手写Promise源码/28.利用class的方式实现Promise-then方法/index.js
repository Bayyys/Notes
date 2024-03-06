//立即执行函数(IIFE)
//好处：可以避免对外部的变量造成污染
(function (window) {
    //声明Promise类
    class Promise {
        //executor表示的是执行器函数
        constructor(executor) {
            //构造器中的this指向表示的是实例化对象

            //添加状态
            this.PromiseState = 'pending';
            //添加结果
            this.PromiseResult = undefined;
            //添加回调函数的数组
            this.callbackFn = [];

            //定义resolve函数
            //箭头函数中的定义，如果形式参数只有一个，那么是可以省略小括号的
            const _resolve = value => {
                //如果实例化对象的状态已经不是pending了，则不需要再更改
                if (this.PromiseState !== 'pending') return;
                this.PromiseState = 'fulfilled';
                this.PromiseResult = value;
                this.callbackFn.forEach(item => {
                    item.onfulfilled();
                })
            }

            //定义reject函数
            //箭头函数是没有自己的this指向的，取决于当前函数所声明的位置的this指向(外层函数中的this指向)
            const _reject = value => {
                if (this.PromiseState !== 'pending') return;
                this.PromiseState = 'rejected';
                this.PromiseResult = value;
                this.callbackFn.forEach(item => {
                    item.onrejected();
                })
            }

            try {
                //调用执行器函数
                executor(_resolve, _reject);
            } catch (err) {
                _reject(err);
            }
        }
        //在类的原型身上添加方法
        then(onfulfilled, onrejected) {
            //第一：用户是否添加了成功回调和失败回调，如果没有添加则需要设置默认值
            if (!(onfulfilled instanceof Function)) onfulfilled = value => value;
            if (!(onrejected instanceof Function)) onrejected = reason => { throw reason };

            //第二：then方法的返回值为新的Promise对象
            return new Promise((resolve, reject) => {
                //封装函数
                const _common = function (callback) {
                    setTimeout(() => {
                        try {
                            //获取不同回调函数(成功回调/失败回调)中的结果
                            const value = callback(this.PromiseResult);
                            if (value instanceof Promise) {
                                value.then(resolve, reject)
                            } else {
                                resolve(value);
                            }
                        } catch (err) {
                            reject(err);
                        }
                    })
                }
                //判断当下实例化对象的状态
                if (this.PromiseState === 'fulfilled') _common.call(this, onfulfilled)
                else if (this.PromiseState === 'rejected') _common.call(this, onrejected)
                else {
                    this.callbackFn.push({
                        onfulfilled: _common.bind(this, onfulfilled),
                        onrejected: _common.bind(this, onrejected),
                    })
                }
            })
        }
    }
    window.Promise = Promise;
})(window); 