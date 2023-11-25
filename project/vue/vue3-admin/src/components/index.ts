import SvgIcon from '@/components/SvgIcon/index.vue'
import Pagination from '@/components/Pagination/index.vue'
import type { App, Component } from 'vue'
const components: { [name: string]: Component } = { SvgIcon, Pagination }
// 注册全局组件
export default {
  // install方法必须有
  install(app: App) {
    // 注册项目中的全局组件
    Object.keys(components).forEach((key: string) => {
      app.component(key, components[key])
    })
  },
}
