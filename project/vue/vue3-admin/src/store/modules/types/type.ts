// 定义小仓库数据state类型
import type { RouteRecordRaw } from 'vue-router'

export interface UserState {
  token: string
  menuRoutes: RouteRecordRaw[]
}
