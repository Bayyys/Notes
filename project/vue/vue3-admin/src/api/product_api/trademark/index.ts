// 品牌管理模块接口
import request from '@/utils/request'
import type { TradeMarkResponseData } from './type'

// 接口地址
enum API {
  TRADEMART_URL = '/admin/product/baseTrademark/',
}

// 获取品牌列表
export const reqHasTrademark = (page: number, limit: number) =>
  request.get<any, TradeMarkResponseData>(
    API.TRADEMART_URL + `${page}/${limit}`,
  )
