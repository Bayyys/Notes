// 属性管理模块接口
import request from '@/utils/request'

enum API {
  C1_URL = '/admin/product/getCategory1',
  C2_URL = '/admin/product/getCategory2',
  C3_URL = '/admin/product/getCategory3',
}

// 获取一级分类
export const reqC1 = () => request.get<any, any>(API.C1_URL)

// 获取二级分类
export const reqC2 = (category1Id: string | number) =>
  request.get<any, any>(API.C2_URL + `/${category1Id}`)

// 获取三级分类
export const reqC3 = (category2Id: string | number) =>
  request.get<any, any>(API.C3_URL + `/${category2Id}`)
