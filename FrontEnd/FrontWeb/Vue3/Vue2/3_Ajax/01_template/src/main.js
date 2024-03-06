import Vue from 'vue'
import App from './App.vue'

Vue.config.productionTip = false

new Vue({
  el: '#root',
  render: h => h(App),
  beforeCreate() {
    Vue.prototype.$bus = this
  }
})
