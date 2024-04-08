var vm = new Vue({
  // 配置对象
  el: '.container',
  data: {
    // 界面数据
    title: '淘东手机',
    goods: goods,
  },
  // 计算属性
  computed: {
    count: function () {
      var sum = 0;
      for (var i = 0; i < this.goods.length; i++) {
        sum += this.goods[i].choose;
      }
      return sum;
    },
  },
});
