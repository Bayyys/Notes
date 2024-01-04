// 路由鉴权
import router from '@/router'
// 1. 路由切换进度条
import nprogress from 'nprogress'
// 引入进度条样式
import 'nprogress/nprogress.css'
// 获取用户仓库
import useUserStore from './store/modules/user'
import setting from './setting'

// 配置进度条(禁用进度环)
nprogress.configure({ showSpinner: false })

// 全局守卫: 项目中任意路由切换会触发的钩子
// 全局前置守卫: 路由切换之前触发
router.beforeEach(async (to: any, from: any, next: any) => {
  document.title = to.meta.title || setting.title
  // to: 即将要进入的目标路由对象
  // from: 当前导航正要离开的路由
  // next: 调用该方法后，才能进入下一个钩子(路由放行函数)
  nprogress.start()
  const userStore = useUserStore()
  const token = userStore.token
  // 获取用户信息
  const username = userStore.username
  // 用户已登录
  if (token) {
    if (to.path === '/login') {
      next({ path: '/' })
    } else {
      if (username) {
        next()
      } else {
        try {
          await userStore.userInfo()
          next()
        } catch (error) {
          await userStore.userLogout()
          next({ path: '/login', query: { redirect: to.path } })
        }
      }
    }
  } else {
    if (to.path === '/login') {
      next()
    } else {
      next({
        path: '/login',
        query: {
          redirect: to.path,
        },
      })
    }
  }
})

// 全局后置守卫: 路由切换之后触发
router.afterEach((route: any) => {
  nprogress.done()
})

// 2. 路由鉴权
// 全部路由组件: 登录|404|任意路由|首页|数据大屏|权限管理(3)|商品管理(4)
// 用户未登录: 只能访问登录页面(login)
// 用户已登录: 可以访问除了登录页面(login)之外的其他页面 [login跳转首页]
