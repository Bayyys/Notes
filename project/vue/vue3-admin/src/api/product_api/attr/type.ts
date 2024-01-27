// 分类API接口相关数据类型
// 接口相应基本数据类型
export interface ResponseData {
  code: number
  message: string
  ok: boolean
}

// 分类的基本数据类型
export interface CategoryObj {
  id: number | string
  name: string
  category1Id?: number
  category2Id?: number
}

// 分类接口响应数据类型
export interface CategoryResponseData extends ResponseData {
  data: CategoryObj[]
}

// 属性接口数据类型
// 属性值对象数据类型
export interface AttrValue {
  id?: number
  valueName: string
  attrId?: number
  flag?: boolean // 控制属性值编辑的显示与隐藏
}

// 属性值数组类型
export type AttrValueList = AttrValue[]

// 属性对象
export interface Attr {
  id?: number
  attrName: string
  categoryId: number | string
  categoryLevel: number
  attrValueList: AttrValueList
  attrIdAndValueId?: string
}

export type AttrList = Attr[]

// 属性接口返回数据类型
export interface AttrResponseData extends ResponseData {
  data: AttrList
}
