import Vue from 'vue'
import App from './App'
// 只需要写目录名称即可，可以自动扫描内部的index.js
import router from './router'

Vue.config.productionTip = false

new Vue({
  el: '#app',
  // 配置路由
  router,
  components: { App },
  template: '<App/>'
})
