<template>
  <div>
    <el-form label-width="auto">
      <el-form-item label="sku名称">
        <el-input placeholder="请输入SKU名称" v-model="skuParams.skuName" />
      </el-form-item>
      <el-form-item label="价格(元)">
        <el-input
          placeholder="请输入价格(元)"
          type="number"
          v-model="skuParams.price"
        />
      </el-form-item>
      <el-form-item label="重量(克)">
        <el-input
          placeholder="请输入重量(克)"
          type="number"
          v-model="skuParams.weight"
        />
      </el-form-item>
      <el-form-item label="SKU描述">
        <el-input
          placeholder="请输入SKU描述"
          type="textarea"
          v-model="skuParams.skuDesc"
        />
      </el-form-item>
      <el-form-item label="平台属性">
        <el-form :inline="true">
          <el-form-item
            v-for="item in attrArr"
            :key="item.id"
            :label="item.attrName"
          >
            <el-select v-model="item.attrIdAndValueId" placeholder="请选择">
              <el-option
                v-for="attrValue in item.attrValueList"
                :key="attrValue.id"
                :label="attrValue.valueName"
                :value="`${item.id}:${attrValue.id}`"
              ></el-option>
            </el-select>
          </el-form-item>
        </el-form>
      </el-form-item>
      <el-form-item label="销售属性">
        <el-form :inline="true">
          <el-form-item
            v-for="item in saleArr"
            :key="item.id"
            :label="item.saleAttrName"
          >
            <el-select v-model="item.saleIdAndValueId" placeholder="请选择">
              <el-option
                v-for="saleAttrValue in item.spuSaleAttrValueList"
                :key="saleAttrValue.id"
                :label="saleAttrValue.saleAttrValueName"
                :value="`${item.id}:${saleAttrValue.id}`"
              ></el-option>
            </el-select>
          </el-form-item>
        </el-form>
      </el-form-item>
      <el-form-item label="图片名称">
        <el-table
          ref="imgTableRef"
          :data="imgArr"
          :style="{ width: '100%' }"
          :border="true"
        >
          <el-table-column type="selection"></el-table-column>
          <el-table-column label="图片" prop="imgUrl">
            <template v-slot="{ row }">
              <el-image
                :src="row.imgUrl"
                style="width: 100px; height: 100px"
              ></el-image>
            </template>
          </el-table-column>
          <el-table-column label="名称" prop="imgName"></el-table-column>
          <el-table-column label="操作" align="center">
            <template v-slot="row">
              <el-button
                type="warning"
                size="small"
                @click="handlerSetDefaultImg(row.row)"
              >
                设置默认
              </el-button>
            </template>
          </el-table-column>
        </el-table>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" icon="DocumentAdd" @click="save">
          保存
        </el-button>
        <el-button type="default" icon="Failed" @click="cancel">取消</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script setup lang="ts">
import {
  SaleAttr,
  SaleAttrResponseData,
  SkuData,
  SpuData,
  SpuHasImg,
  SpuImg,
} from '@/api/product_api/spu/type'
import { reqAttr } from '@/api/product_api/attr'
import { AttrList, AttrResponseData } from '@/api/product_api/attr/type'
import {
  reqAddSku,
  reqSpuHasSaleAttr,
  reqSpuImageList,
} from '@/api/product_api/spu'
import { reactive, ref } from 'vue'
import { ElMessage } from 'element-plus'

let $emit = defineEmits(['changeScene'])

let imgTableRef = ref<any>(null)
let attrArr = ref<AttrList>([])
let saleArr = ref<SaleAttr[]>([])
let imgArr = ref<SpuImg[]>([])
let skuParams = reactive<SkuData>({
  category3Id: 0,
  spuId: 0,
  tmId: 0,
  skuName: '',
  price: 0,
  weight: 0,
  skuDesc: '',
  skuAttrValueList: [],
  skuSaleAttrValueList: [],
  skuDefaultImg: '',
})

// 对父组件暴露方法-初始化表单数据
const initSKUData = async (C1Id: number, C2Id: number, row: SpuData) => {
  const { category3Id: C3Id, id: SPUId, tmId } = row
  skuParams.category3Id = C3Id
  skuParams.spuId = SPUId as number
  skuParams.tmId = tmId
  // 获取平台属性
  const res1: AttrResponseData = await reqAttr(C1Id, C2Id, C3Id)
  attrArr.value = res1.data
  // 获取对应的销售属性
  const res2: SaleAttrResponseData = await reqSpuHasSaleAttr(SPUId as number)
  console.log(res2)
  saleArr.value = res2.data
  // 获取照片墙的数据
  const res3: SpuHasImg = await reqSpuImageList(SPUId as number)
  imgArr.value = res3.data
}

// 设置默认图片按钮点击回调事件
const handlerSetDefaultImg = (row: any) => {
  imgTableRef.value.clearSelection()
  imgTableRef.value.toggleRowSelection(row)
  skuParams.skuDefaultImg = row.imgUrl as string
}

// 表单保存按钮的回调
const save = async () => {
  // 整理参数
  // 平台属性
  skuParams.skuAttrValueList = attrArr.value.reduce((pre: any[], next: any) => {
    const attrIdAndValueId = next.attrIdAndValueId
    if (attrIdAndValueId) {
      const [attrId, attrValueId] = attrIdAndValueId.split(':')
      pre.push({
        attrId: Number(attrId),
        attrValueId: Number(attrValueId),
      })
    }
    return pre
  }, [] as any[])
  // 销售属性
  skuParams.skuSaleAttrValueList = saleArr.value.reduce(
    (pre: any[], next: any) => {
      const saleIdAndValueId = next.saleIdAndValueId
      if (saleIdAndValueId) {
        const [saleAttrId, saleAttrValueId] = saleIdAndValueId.split(':')
        pre.push({
          saleAttrId: Number(saleAttrId),
          saleAttrValueId: Number(saleAttrValueId),
        })
      }
      return pre
    },
    [] as any[],
  )
  // 发送请求
  const res = await reqAddSku(skuParams)
  if (res.code === 200) {
    ElMessage.success('添加成功')
    $emit('changeScene', { scene: 0, returnFirstPage: false })
  } else {
    ElMessage.error('添加失败')
    $emit('changeScene', { scene: 0, returnFirstPage: false })
  }
}

// 表单取消按钮的回调
const cancel = () => {
  $emit('changeScene', { scene: 0, addFlag: false })
}

defineExpose({
  initSKUData,
})
</script>

<style scoped></style>
