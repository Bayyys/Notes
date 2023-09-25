// 引入的不再是Vue构造函数了，引入的是一个名为createApp的工厂函数
import { createApp } from 'vue'
// 与Vue2不同的是, 不存在Vue这个变量
import App from './App.vue'

// 创建应用实例对象——app(类似于之前的vm，但app比vm更"轻")
const app = createApp(App)
// console.log("app", app) 
app.mount('#app')