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

            //定义resolve函数
            //箭头函数中的定义，如果形式参数只有一个，那么是可以省略小括号的
            const _resolve = value => {
                //如果实例化对象的状态已经不是pending了，则不需要再更改
                if (this.PromiseState !== 'pending') return;
                this.PromiseState = 'fulfilled';
                this.PromiseResult = value;
            }

            //定义reject函数
            //箭头函数是没有自己的this指向的，取决于当前函数所声明的位置的this指向(外层函数中的this指向)
            const _reject = value => {
                if (this.PromiseState !== 'pending') return;
                this.PromiseState = 'rejected';
                this.PromiseResult = value;
            }

            try {
                //调用执行器函数
                executor(_resolve, _reject);
            } catch (err) {
                _reject(err);
            }
        }
    }
    window.Promise = Promise;
})(window); 