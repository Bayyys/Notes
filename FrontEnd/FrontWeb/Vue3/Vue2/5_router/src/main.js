import Vue from 'vue'
import App from './App.vue'
// 引入VueRouter
import VueRouter from "vue-router";
import router from './router';
// VueRouter插件使用
Vue.use(VueRouter);

Vue.config.productionTip = false

new Vue({
  el: '#app',
  render: h => h(App),
  router: router, // 配置路由器
})
