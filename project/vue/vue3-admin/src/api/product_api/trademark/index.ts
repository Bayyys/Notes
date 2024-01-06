// 品牌管理模块接口
import request from '@/utils/request'
import type { TradeMarkResponseData, Trademark } from './type'

// 接口地址
enum API {
  TRADEMARK_URL = '/admin/product/baseTrademark/',
  ADDTRADMARK_URL = '/admin/product/baseTrademark/save',
  UPDATETRADEMARK_URL = '/admin/product/baseTrademark/update',
  DELETETRADEMARK_URL = '/admin/product/baseTrademark/remove/',
}

// 获取品牌列表
export const reqHasTrademark = (page: number, limit: number) =>
  request.get<any, TradeMarkResponseData>(
    API.TRADEMARK_URL + `${page}/${limit}`,
  )

// 添加/修改品牌
export const reqAddOrUpdateTrademark = (trademark: Trademark) => {
  if (trademark.id) {
    // 修改trademark
    return request.put<any, any>(API.UPDATETRADEMARK_URL, trademark)
  } else {
    // 新增trademark
    return request.post<any, any>(API.ADDTRADMARK_URL, trademark)
  }
}

// 删除品牌
export const reqDeleteTrademark = (id: number) =>
  request.delete<any, any>(API.DELETETRADEMARK_URL + id)
