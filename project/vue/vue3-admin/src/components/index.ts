// svg组件
import SvgIcon from '@/components/SvgIcon/index.vue'
// 分页器组件
import Pagination from '@/components/Pagination/index.vue'
// element-plus: Icon组件
import * as ElementPlusIconsVue from '@element-plus/icons-vue'
// 输出测试: console.log(ElementPlusIconsVue)
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
    // 将 element-plus 提供的Icon组件注册为全局组件
    for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
      app.component(key, component)
    }
  },
}
