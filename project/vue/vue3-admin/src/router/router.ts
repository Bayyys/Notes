// 对外暴露配置路由(常量路由表)
export const constantRoute = [
  {
    // 登录路由
    path: '/login',
    component: () => import('@/views/login/index.vue'), // 路由懒加载
    name: 'login', // 命名路由 (权限管理时使用)
  },
  {
    // 登录成功后, 展示数据的路由
    path: '/',
    component: () => import('@/layout/index.vue'),
    name: 'layout',
  },
  {
    // 404路由
    path: '/404',
    component: () => import('@/views/404/index.vue'),
    name: '404',
  },
  {
    // 重定向: 如果访问的路由不存在, 重定向到404路由
    path: '/:pathMatch(.*)*',
    redirect: '/404',
    name: 'Any',
  },
]
