import request from '@/utils/request'
import type { HasSPUResponseData } from './type'

enum API {
  HASSPU_URL = '/admin/product/',
}

// 获取SPU数据
export const reqHasSPU = (page: number, limit: number, C3ID: string | number) =>
  request.get<any, HasSPUResponseData>(
    API.HASSPU_URL + `${page}/${limit}?category3Id=${C3ID}`,
  )
