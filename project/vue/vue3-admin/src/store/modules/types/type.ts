// 定义小仓库数据state类型
import type { RouteRecordRaw } from 'vue-router'
import type { CategoryObj } from '@/api/product_api/attr/type'

export interface UserState {
  token: string
  menuRoutes: RouteRecordRaw[]
  username: string
  avatar: string
}

export interface CategoryState {
  // 一级分类列表
  C1Arr: CategoryObj[]
  // 一级分类Id
  C1Id: string | number
  // 二级分类列表
  C2Arr: CategoryObj[]
  // 二级分类Id
  C2Id: string | number
  // 三级分类列表
  C3Arr: CategoryObj[]
  // 三级分类Id
  C3Id: string | number
}
