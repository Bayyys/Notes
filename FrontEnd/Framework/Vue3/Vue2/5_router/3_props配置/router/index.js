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
      name: "myHome",
      // 路由路径
      path: "/home",
      // 路由组件
      component: Home,
      children: [
        {
          name: "myNews",
          path: "news", // 不要多加 '/' 子路由会自动拼接父路由
          component: News,
        },
        {
          name: "myMessage",
          path: "message",
          component: Message,
          children: [
            {
              name: "myDetail",
              path: "detail/:id/:title",
              component: Detail,
              // 直接传递props参数, 值为对象, 该对象中的所有key-value都会以props的形式传给Detail组件
              // props: {
              //   id: "002",
              //   title: "message002",
              // },

              // props: true, // 将params参数作为props传给Detail组件
              // props: true,

              // 函数形式
              props($route) {
                return {
                  id: $route.params.id,   // 从params中取值
                  title: $route.params.title,  // 也可以从query中取值
                };
              },
            },
          ],
        },
      ],
    },
    {
      name: "myAbout",
      path: "/about",
      component: About,
    },
  ],
});
