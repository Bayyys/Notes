// 属性管理模块接口
import request from '@/utils/request'
import { CategoryResponseData, AttrResponseData, Attr } from './type'

enum API {
  C1_URL = '/admin/product/getCategory1',
  C2_URL = '/admin/product/getCategory2',
  C3_URL = '/admin/product/getCategory3',
  ATTR_URL = '/admin/product/attrInfoList', // 获取属性列表(指定1/2/3级分类Id)
  ADDORUPDATEATTR_UTL = '/admin/product/saveAttrInfo', // 添加或修改属性
  DELETEATTR_URL = '/admin/product/deleteAttr', // 删除属性
}

// 获取一级分类
export const reqC1 = () => request.get<any, CategoryResponseData>(API.C1_URL)

// 获取二级分类
export const reqC2 = (category1Id: string | number) =>
  request.get<any, CategoryResponseData>(API.C2_URL + `/${category1Id}`)

// 获取三级分类
export const reqC3 = (category2Id: string | number) =>
  request.get<any, CategoryResponseData>(API.C3_URL + `/${category2Id}`)

// 获取属性列表
export const reqAttr = (
  category1Id: string | number,
  category2Id: string | number,
  category3Id: string | number,
) =>
  request.get<any, AttrResponseData>(
    API.ATTR_URL + `/${category1Id}/${category2Id}/${category3Id}`,
  )

// 添加或修改属性
export const reqAddOrUpdateAttr = (attr: Attr) =>
  request.post<any, any>(API.ADDORUPDATEATTR_UTL, attr)

// 删除属性
export const reqDeleteAttr = (attrId: string | number) =>
  request.delete<any, any>(API.DELETEATTR_URL + `/${attrId}`)
