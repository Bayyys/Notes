// 引入VueRouter
import VueRouter from "vue-router";
import Home from "../pages/Home";
import About from "../pages/About";
import News from "../pages/News";
import Message from "../pages/Message";
import Detail from "../pages/Detail";

// 创建并暴露一个路由器
export default new VueRouter({
  // 配置路由
  routes: [
    // 每个路由都是一个对象
    {
      name: 'myHome',
      // 路由路径
      path: "/home",
      // 路由组件
      component: Home,
      children: [
        {
          name: 'myNews',
          path: "news", // 不要多加 '/' 子路由会自动拼接父路由
          component: News
        },
        {
          name: 'myMessage',
          path: "message",
          component: Message,
          children: [
            {
              name: 'myDetail',
              path: "detail",
              component: Detail,
            }
          ]
        },
      ],
    },
    {
      name: 'myAbout',
      path: "/about",
      component: About,
    },
  ],
});
