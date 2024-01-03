import { defineStore } from 'pinia'

const useLayoutSettingStore = defineStore('SettingStore', {
  state: () => {
    return {
      fold: false, // 侧边栏是否折叠
      refresh: false, // 是否刷新页面
    }
  },
})

export default useLayoutSettingStore
