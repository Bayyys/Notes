/* 
    整个项目的入口文件
*/

// 引入 Vue
import { createApp } from 'vue'

// 引入 App 组件, 作为所有组件的父组件
import App from './App.vue'

// 创建Vue实例对象——vm
createApp(App).mount('#app')
