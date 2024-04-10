import Vue from 'vue'
import App from './App.vue'
// 引入store
import store from './store'

Vue.config.productionTip = false

new Vue({
  el: '#app',
  store,  // 配置store
  render: h => h(App),
  beforeCreate() {
    Vue.prototype.$bus = this
  }
})
