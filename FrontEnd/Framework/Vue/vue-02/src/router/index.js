import Vue from 'vue'
import VueRouter  from "vue-router";

import Content from "../components/Content.vue";
import Main from "../components/Main.vue";

// 安装路由
Vue.use(VueRouter);

export default new VueRouter({
  routes: [
    {
      // 路由路径
      name: 'content',
      path: '/content',
      // 跳转组件
      component: Content
    },
    {
      name: 'main',
      path: '/main',
      component: Main
    }
  ]
})
