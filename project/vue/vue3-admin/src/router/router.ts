// 对外暴露配置路由(常量路由表)
export const constantRoute = [
  {
    // 登录路由
    path: '/login',
    component: () => import('@/views/login/index.vue'), // 路由懒加载
    name: 'login', // 命名路由 (权限管理时使用)
    meta: {
      title: '登录', // 菜单标题
      hidden: true, // 是否在菜单中隐藏该路由
    },
  },
  {
    // 登录成功后, 展示数据的路由
    path: '/',
    component: () => import('@/layout/index.vue'),
    name: 'layout',
    meta: {
      title: 'layout',
      hidden: false,
    },
    children: [
      {
        path: '/home',
        component: () => import('@/views/home/index.vue'),
        meta: {
          title: '首页',
          hidden: false,
        },
      },
      {
        path: '/test',
        component: () => import('@/views/home/index.vue'),
        meta: {
          title: '测试',
          hidden: false,
        },
      },
    ],
  },
  {
    // 404路由
    path: '/404',
    component: () => import('@/views/404/index.vue'),
    name: '404',
    meta: {
      title: '404',
      hidden: true,
    },
  },
  {
    // 重定向: 如果访问的路由不存在, 重定向到404路由
    path: '/:pathMatch(.*)*',
    redirect: '/404',
    name: 'Any',
    meta: {
      title: 'Any',
      hidden: true,
    },
  },
]
