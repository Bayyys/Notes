import { defineStore } from 'pinia'

const useLayoutSettingStore = defineStore('SettingStore', {
  state: () => {
    return {
      fold: false,
    }
  },
})

export default useLayoutSettingStore
