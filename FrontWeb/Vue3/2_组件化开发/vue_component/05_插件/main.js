// 引入Vue
import { createApp } from 'vue'

// 引入App组件
import App from './App.vue'

// 引入插件
import plugins from './plugins'

// 创建Vue实例对象---vm
const app = createApp(App)
app.mount('#app')
app.use(plugins)