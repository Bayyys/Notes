// 引入VueRouter
import VueRouter from "vue-router";
import Home from "../pages/Home";
import About from "../pages/About";
import News from "../pages/News";
import Message from "../pages/Message";
import Detail from "../pages/Detail";

// 创建并暴露一个路由器
const router = new VueRouter({
  // 配置路由
  routes: [
    // 每个路由都是一个对象
    {
      name: "myHome",
      // 路由路径
      path: "/home",
      // 路由组件
      component: Home,
      meta: { isAuth: false, title: '主页' }, // 路由元信息, 此处false的内容也可以省略
      children: [
        {
          name: "myNews",
          path: "news", // 不要多加 '/' 子路由会自动拼接父路由
          meta: { isAuth: true, title: '新闻' },
          component: News,
          beforeEnter: (to, from, next) => {
            console.log("独享路由守卫", to, from);
            if (to.meta.isAuth) {
              if (localStorage.getItem("name") === "admin") {
                next();
              } else {
                alert("无权访问");
              }
            } else {
              next();
            }
          },
        },
        {
          name: "myMessage",
          path: "message",
          meta: { isAuth: true, title: '消息' },
          component: Message,
          beforeEnter: (to, from, next) => {
            console.log("独享路由守卫", to, from);
            if (to.meta.isAuth) {
              if (localStorage.getItem("name") === "admin") {
                next();
              } else {
                alert("无权访问");
              }
            } else {
              next();
            }
          },
          children: [
            {
              name: "myDetail",
              path: "detail/:id/:title",
              component: Detail,
              props($route) {
                return {
                  id: $route.params.id, // 从params中取值
                  title: $route.params.title, // 也可以从query中取值
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
      meta: { title: '关于' },
    },
  ],
});

// 全局前置路由守卫——初始化时被调用、每次路由切换之前被调用
// router.beforeEach((to, from, next) => {
//   console.log("beforeEach", to, from);
//   if (to.meta.isAuth) {
//     if (localStorage.getItem("name") === "admin") {
//       next();
//     } else {
//       alert("无权访问");
//     }
//   } else {
//     next();
//   }
// });

// 全局后置路由守卫——初始化时被调用、每次路由切换之后被调用
router.afterEach((to, from) => {
  console.log("afterEach", to, from);
  document.title = to.meta.title || 'Vue3';
});

export default router;
