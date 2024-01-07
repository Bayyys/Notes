// 商品分类
import { defineStore } from 'pinia'
import { reqC1, reqC2, reqC3 } from '@/api/product_api/attr'
import type { CategoryResponseData } from '@/api/product_api/attr/type'
import type { CategoryState } from './types/type'

const useCategoryStore = defineStore('CategoryStore', {
  state: (): CategoryState => {
    return {
      // 一级分类列表
      C1Arr: [],
      // 一级分类Id
      C1Id: '',
      // 二级分类列表
      C2Arr: [],
      // 二级分类Id
      C2Id: '',
      // 三级分类列表
      C3Arr: [],
      // 三级分类Id
      C3Id: '',
    }
  },
  actions: {
    // 获取一级分类
    async getC1() {
      this.C2Id = ''
      this.C3Arr = []
      this.C3Id = ''
      const res: CategoryResponseData = await reqC1()
      if (res.code === 200) {
        this.C1Arr = res.data
        return 'ok'
      } else {
        return Promise.reject(new Error('获取一级分类失败'))
      }
    },
    // 获取二级分类
    async getC2() {
      this.C2Id = ''
      this.C3Arr = []
      this.C3Id = ''
      const res: CategoryResponseData = await reqC2(this.C1Id)
      if (res.code === 200) {
        this.C2Arr = res.data
        return 'ok'
      } else {
        return Promise.reject(new Error('获取二级分类失败'))
      }
    },
    // 获取三级分类
    async getC3() {
      this.C3Arr = []
      this.C3Id = ''
      const res: CategoryResponseData = await reqC3(this.C2Id)
      if (res.code === 200) {
        this.C3Arr = res.data
        return 'ok'
      } else {
        return Promise.reject(new Error('获取三级分类失败'))
      }
    },
  },
})

export default useCategoryStore
