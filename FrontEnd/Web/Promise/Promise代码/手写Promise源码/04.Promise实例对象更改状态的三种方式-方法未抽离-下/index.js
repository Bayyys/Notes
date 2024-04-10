//立即执行函数(IIFE)
//好处：可以避免对外部的变量造成污染
(function (window) {
    //只要是给构造函数的实例化对象身上添加属性/方法，那么直接在函数中this对象的地址引用身上直接添加
    function Promise(executor) {
        //给Promise构造函数所产生的实例化对象身上添加两个属性
        this.PromiseState = 'pending';
        this.PromiseResult = undefined;
        //方法1：可以保存想要的函数中this指向，在哪一个需要的函数进行直接使用即可
        //let _this = this;
        /**
         * 函数中的this指向取决于函数的调用者，也就是说谁调用了这个函数，那么函数中的this就指向谁
         * 函数中this不光可以得到另一个函数中的this指向，还可以直接修改成想要的this指向
         * 修改函数中的this指向三种：call、apply、bind
         * call和apply之间的区别：在于函数中修改完this指向，实际参数传递的格式不同
         * 语法：
         * 函数名.call(新的this指向,实际参数1,实际参数2....)
         * 函数名.apply(新的this指向,[实际参数1,实际参数2....])
         * call和apply之间的共同点：在于函数一旦修改完想要的this指向之后，则函数就会立即执行
         * 
         * call和bind之前的区别：call会立即执行，bind不会立即执行，且bind只有返回值，
         * 且返回的是与原函数结构一模一样的修改完this指向的新函数
         */
        try {
            executor(function (value) {
                this.PromiseState = 'fulfilled';
                this.PromiseResult = value;
            }.bind(this), function (value) {
                this.PromiseState = 'rejected';
                this.PromiseResult = value;
            }.bind(this));
        } catch (e) {
            if (typeof e === 'object') {
                this.PromiseState = 'rejected';
                this.PromiseResult = e.message;
            } else {
                this.PromiseState = 'rejected';
                this.PromiseResult = e;
            }

        }
    }
    window.Promise = Promise;
})(window); 