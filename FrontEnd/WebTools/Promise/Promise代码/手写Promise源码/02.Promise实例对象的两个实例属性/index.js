//立即执行函数(IIFE)
//好处：可以避免对外部的变量造成污染
(function (window) {
    //只要是给构造函数的实例化对象身上添加属性/方法，那么直接在函数中this对象的地址引用身上直接添加
    function Promise(executor) {
        //console.log('实例化对象：', this);

        //给Promise构造函数所产生的实例化对象身上添加两个属性
        this.PromiseState = 'pending';
        this.PromiseResult = undefined;

        executor();
    }
    window.Promise = Promise;
})(window);