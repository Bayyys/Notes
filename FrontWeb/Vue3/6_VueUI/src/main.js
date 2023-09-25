import Vue from "vue";
import App from "./App.vue";
import { Button, DatePicker } from "element-ui";

Vue.config.productionTip = false;

Vue.component(Button.name, Button);
Vue.component(DatePicker.name, DatePicker);
/* 或写为
 * Vue.use(Button)
 * Vue.use(DatePicker)
 */

new Vue({
  el: "#app",
  render: (h) => h(App),
  beforeCreate() {
    Vue.prototype.$bus = this;
  },
});
