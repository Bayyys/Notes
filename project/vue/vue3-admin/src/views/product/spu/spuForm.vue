<template>
  <div>
    <el-form label-width="100px" label-position="left">
      <el-form-item label="SPU名称">
        <el-input placeholder="请输入SPU名称" v-model="SpuParams.spuName" />
      </el-form-item>
      <el-form-item label="SPU品牌">
        <el-select placeholder="请选择" v-model="SpuParams.tmId">
          <el-option
            v-for="item in TradeMarkList"
            :key="item.id"
            :label="item.tmName"
            :value="item.id"
          />
        </el-select>
      </el-form-item>
      <el-form-item label="SPU描述" prop="description">
        <el-input
          type="textarea"
          placeholder="请输入描述"
          v-model="SpuParams.description"
        />
      </el-form-item>
      <el-form-item label="SPU图片">
        <el-upload
          v-model:file-list="ImgList"
          action="/api/admin/product/fileUpload"
          list-type="picture-card"
          :on-preview="handlePictureCardPreview"
          :on-remove="handleRemove"
          :before-upload="handleUpload"
        >
          <el-icon><Plus /></el-icon>
        </el-upload>
        <el-dialog v-model="dialogVisible">
          <img
            w-full
            :src="dialogImageUrl"
            alt="Preview Image"
            style="width: 100%; height: 100%"
          />
        </el-dialog>
      </el-form-item>
      <el-form-item label="SPU销售属性">
        <!-- 展示销售属性的下拉菜单 -->
        <el-select
          :placeholder="
            unSelectSaleAttr.length
              ? `尚有${unSelectSaleAttr.length}项可选`
              : '暂无可选项目'
          "
          v-model="saleAttrId"
        >
          <el-option
            v-for="item in unSelectSaleAttr"
            :key="item.id"
            :label="item.name"
            :value="item.id"
          />
        </el-select>
        <el-button
          icon="Plus"
          type="primary"
          style="margin-left: 10px"
          :disabled="saleAttrId ? false : true"
          @click="addSaleAttr"
        >
          添加属性值
        </el-button>
        <el-table
          :style="{ width: '100%', margin: '10px 0px' }"
          border
          :data="SaleAttrList"
        >
          <el-table-column
            label="序号"
            type="index"
            align="center"
            width="80px"
          />
          <!-- 销售属性名 -->
          <el-table-column
            label="销售属性名"
            width="120px"
            prop="saleAttrName"
          ></el-table-column>
          <!-- 销售属性值 -->
          <el-table-column label="销售属性值">
            <template v-slot="{ row, $index }">
              <el-tag
                v-for="item in row.spuSaleAttrValueList"
                :key="item.id"
                :style="{ marginRight: '6px' }"
                closable
                @close="row.spuSaleAttrValueList.splice($index, 1)"
              >
                {{ item.saleAttrValueName }}
              </el-tag>
              <el-input
                :ref="(vc: any) => (inputArr[$index] = vc)"
                v-model="row.saleAttrValue"
                v-if="row.flag === true"
                placeholder="请输入"
                size="small"
                style="width: 100px"
                @blur="toLook(row)"
              />
              <el-button
                v-else
                type="primary"
                size="small"
                icon="Plus"
                @click="toEdit(row, $index)"
              ></el-button>
            </template>
          </el-table-column>
          <!-- 属性操作 -->
          <el-table-column label="属性操作" width="120px">
            <template v-slot="{ $index }">
              <el-button
                type="danger"
                size="small"
                icon="Delete"
                @click="SaleAttrList.splice($index, 1)"
              ></el-button>
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
import { ref, computed, nextTick } from 'vue'
import type {
  AllTradeMark,
  HasSaleAttr,
  HasSaleAttrResponseData,
  SaleAttr,
  SaleAttrResponseData,
  SpuData,
  SpuHasImg,
  SpuImg,
  Trademark,
} from '@/api/product_api/spu/type'
import {
  reqAllTradeMark,
  reqAllSaleAttr,
  reqSpuImageList,
  reqSpuHasSaleAttr,
  reqAddOrUpdateSpu,
} from '@/api/product_api/spu'
import { ElMessage } from 'element-plus'

let $emit = defineEmits(['changeScene'])

let SpuParams = ref<SpuData>({
  category3Id: '',
  spuName: '',
  description: '',
  tmId: '',
  spuImageList: [],
  spuSaleAttrList: [],
}) // 父组件传递过来的数据

let TradeMarkList = ref<Trademark[]>([]) // 已有的品牌列表
let ImgList = ref<SpuImg[]>([]) // 图片列表
let SaleAttrList = ref<SaleAttr[]>([]) // 已有销售属性列表
let HasSaleAttrList = ref<HasSaleAttr[]>([]) // 销售属性列表

let dialogVisible = ref<boolean>(false) // 是否显示图片预览
let dialogImageUrl = ref<string>('') // 图片预览的url

let saleAttrId = ref<number | string>('') // 销售属性id和name
let inputArr = ref<any[]>([]) // input框数组

// 取消按钮点击回调
const cancel = () => {
  $emit('changeScene', { scene: 0, addFlag: false })
}

// 保存按钮点击回调
const save = async () => {
  // 整理参数
  SpuParams.value.spuImageList = ImgList.value.map((item: any) => {
    return {
      imgUrl: (item.response && item.response.data) || item.url,
      imgName: item.name,
    }
  })
  SpuParams.value.spuSaleAttrList = SaleAttrList.value
  // 发送参数
  const res = await reqAddOrUpdateSpu(SpuParams.value)
  if (res.code === 200) {
    ElMessage.success(`${SpuParams.value.id ? '修改' : '添加'}成功`)
    $emit('changeScene', {
      scene: 0,
      addFlag: SpuParams.value.id ? false : true,
    })
  } else {
    ElMessage.error(`${SpuParams.value.id ? '修改' : '添加'}失败`)
  }
}

// 图片预览回调
const handlePictureCardPreview = (uploadFile: any) => {
  dialogVisible.value = true
  dialogImageUrl.value = uploadFile.url
}

// 图片移除回调
const handleRemove = (file: any) => {
  console.log(file)
}

// 图片上传前回调(约束文件类型和大小)
const handleUpload = (rawFile: any) => {
  if (
    rawFile.type !== 'image/jpeg' &&
    rawFile.type !== 'image/png' &&
    rawFile.type !== 'image/gif'
  ) {
    // 上传文件格式: JPG、PNG、GIF
    ElMessage.error('上传图片格式错误(仅支持JPG、PNG、GIF格式)')
    return false
  } else if (rawFile.size / 1024 / 1024 > 2) {
    // 上传文件大小: 2MB
    ElMessage.error('上传图片大小不能超过2MB')
    return false
  }
  return true
}

// 添加销售属性值
const addSaleAttr = () => {
  if (
    !saleAttrId.value ||
    SaleAttrList.value.find((item) => item.baseSaleAttrId === saleAttrId.value)
  )
    return
  SaleAttrList.value.push({
    baseSaleAttrId: saleAttrId.value as number,
    saleAttrName: HasSaleAttrList.value.find((item) => {
      return item.id === saleAttrId.value
    })?.name as string,
    spuSaleAttrValueList: [],
  })
  saleAttrId.value = ''
}

// 属性值编辑
const toEdit = (row: SaleAttr, $index: number) => {
  row.flag = true
  nextTick(() => {
    inputArr.value[$index].focus()
  })
}

// 属性值查看
const toLook = (row: SaleAttr) => {
  const saleAttrValue = row.saleAttrValue?.trim() as string
  const baseSaleAttrId = row.baseSaleAttrId
  let error_flag = true
  if (!saleAttrValue) {
    ElMessage.error('属性值不能为空')
    error_flag = false
  }
  if (
    row.spuSaleAttrValueList.find((item) => {
      return item.saleAttrValueName === saleAttrValue
    })
  ) {
    ElMessage.error('该属性值不能重复')
    error_flag = false
  }
  if (error_flag)
    row.spuSaleAttrValueList.push({
      baseSaleAttrId,
      saleAttrValueName: saleAttrValue,
    })
  row.flag = false
  row.saleAttrValue = ''
}

// 未选中的销售属性
let unSelectSaleAttr = computed(() => {
  return HasSaleAttrList.value.filter((item1) => {
    return SaleAttrList.value.every((item2) => {
      return item2.saleAttrName !== item1.name
    })
  })
})

// 初始化已有SPU请求方法
const initHasSpu = async (spu: SpuData) => {
  // spu为父组件传递过来的数据
  SpuParams.value = spu
  // 获取全部品牌数据
  const res1: AllTradeMark = await reqAllTradeMark()
  // 获取品牌下销售图片
  const res2: SpuHasImg = await reqSpuImageList(spu.id as number)
  // 获取品牌下已有的销售属性值
  const res3: SaleAttrResponseData = await reqSpuHasSaleAttr(spu.id as number)
  // 获取全部销售属性
  const res4: HasSaleAttrResponseData = await reqAllSaleAttr()
  TradeMarkList.value = res1.data
  ImgList.value = res2.data.map((item) => {
    return {
      name: item.imgName,
      url: item.imgUrl,
    }
  })
  SaleAttrList.value = res3.data
  HasSaleAttrList.value = res4.data
}

// 新增SPU初始化请求方法
const initAddSPU = async (C3Id: string | number) => {
  // 清空数据
  SpuParams.value = {
    category3Id: C3Id as number,
    spuName: '',
    description: '',
    tmId: '',
    spuImageList: [],
    spuSaleAttrList: [],
  }
  ImgList.value = []
  SaleAttrList.value = []
  saleAttrId.value = ''
  // 获取全部品牌数据
  const res1: AllTradeMark = await reqAllTradeMark()
  // 获取全部销售属性
  const res2: HasSaleAttrResponseData = await reqAllSaleAttr()
  TradeMarkList.value = res1.data
  HasSaleAttrList.value = res2.data
}

// 对外暴露: 供父组件调用
defineExpose({
  initHasSpu,
  initAddSPU,
})
</script>

<style scoped></style>
