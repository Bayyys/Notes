export interface ResponseData {
  code: number
  message: string
  ok: boolean
}

export interface SPUData {
  id?: number
  spuName: string
  description: string
  category3Id: string | number
  tmId: number
  spuSaleAttrList: null
  spuImageList: null
}

export type Records = SPUData[]

export interface HasSPUResponseData extends ResponseData {
  data: {
    records: Records
    total: number
    size: number
    current: number
    searchCount: boolean
    pages: number
  }
}
