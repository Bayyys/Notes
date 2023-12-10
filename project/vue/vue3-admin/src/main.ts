import { createApp } from 'vue'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
//@ts-expect-error: 配置element-plus国际化
import { zhCn } from 'element-plus/es/locales.mjs'
// SVG插件注册
import 'virtual:svg-icons-register'
// 全局组件注册
import gloablComponent from './components/index'
// 全局样式
import '@/styles/index.scss'
// 路由注册
import router from './router'
// 引入 pinia
import store from './store'
import App from '@/App.vue'
// 递归调用组件
// import MyMenu from '@/layout/menu/index.vue'

const app = createApp(App)
app.use(ElementPlus, {
  locale: zhCn,
})
app.use(gloablComponent)
app.use(router)
app.use(store)
// app.component('MyMenu', MyMenu)
app.mount('#app')
