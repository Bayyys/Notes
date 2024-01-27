<template>
  <div>
    <Category></Category>
    <el-card style="margin: 10px 0px">
      <!-- Card头部: 添加品牌按钮 -->
      <template #header>
        <div class="clearfix">
          <div v-show="scene === 0">
            <el-button
              type="primary"
              icon="Plus"
              :d="categoryStore.C3Id ? false : true"
              @click="addSpu"
            >
              添加SPU
            </el-button>
          </div>
          <h1 v-show="scene === 1">{{ headTitle }}</h1>
          <h1 v-show="scene === 2">添加SKU</h1>
        </div>
      </template>
      <div v-show="scene === 0">
        <el-table :data="records" :style="{ width: '100%' }" order>
          <el-table-column label="序号" type="index" align="center" />
          <el-table-column label="SPU名称" prop="spuName" />
          <el-table-column
            label="SPU描述"
            prop="description"
            show-overflow-tooltip
          />
          <el-table-column label="SPU操作">
            <template v-slot="{ row }">
              <el-button
                type="primary"
                size="small"
                icon="Plus"
                title="添加SKU"
                @click="addSKU(row)"
              ></el-button>
              <el-button
                type="warning"
                size="small"
                icon="Edit"
                title="修改SPU"
                @click="updateSPU(row)"
              ></el-button>
              <el-button
                type="info"
                size="small"
                icon="Location"
                title="查看SKU列表"
              ></el-button>
              <el-popconfirm
                :title="`确认删除${row.attrName}?`"
                icon="Delete"
                icon-color="red"
              >
                <template #reference>
                  <el-button
                    size="small"
                    type="danger"
                    icon="Delete"
                    title="=删除SPU"
                  ></el-button>
                </template>
              </el-popconfirm>
            </template>
          </el-table-column>
        </el-table>
        <el-pagination
          v-model:current-page="pageNum"
          v-model:page-size="pageSize"
          :page-sizes="[3, 5, 7, 9]"
          :small="true"
          :background="true"
          layout="prev, pager, next, jumper, ->, total, sizes"
          :total="total"
          @current-change="getHasSPU"
          @size-change="changeSize"
        />
      </div>
      <SPUFrom
        ref="SPUFormRef"
        v-show="scene === 1"
        @changeScene="changeScene"
      ></SPUFrom>
      <SKUFrom
        ref="SKUFormRef"
        v-show="scene === 2"
        @changeScene="changeScene"
      ></SKUFrom>
      <el-button @click="scene = (scene + 1) % 3">Default</el-button>
    </el-card>
  </div>
</template>

<script setup lang="ts">
import { ref, watch } from 'vue'
import { reqHasSpu } from '@/api/product_api/spu'
import type {
  HasSpuResponseData,
  Records,
  SpuData,
} from '@/api/product_api/spu/type'
import useCategoryStore from '@/store/modules/category'
// 引入相应子组件
import SPUFrom from './spuForm.vue'
import SKUFrom from './skuForm.vue'
let categoryStore = useCategoryStore()
let pageNum = ref<number>(1) // 默认页码
let pageSize = ref<number>(3) // 默认每页显示数
let total = ref<number>(0) // 总条数
let records = ref<Records>([]) // SPU列表
let scene = ref<number>(0) // 场景(0:SPU列表, 1:添加|修改SPU, 2:添加SKU)
let SPUFormRef = ref<any>(null) // SPUForm引用
let SKUFormRef = ref<any>(null) // SKUForm引用
let headTitle = ref<string>('添加SPU') // 头部标题

// 添加SPU按钮回调
const addSpu = () => {
  headTitle.value = '添加SPU'
  SPUFormRef.value.initAddSPU(categoryStore.C3Id)
  scene.value = 1
}

// 修改已有SPU按钮的回调
const updateSPU = (row: SpuData) => {
  headTitle.value = '修改SPU'
  SPUFormRef.value.initHasSpu(row)
  scene.value = 1
}

// 添加SKU按钮回调
const addSKU = (row: SpuData) => {
  scene.value = 2
  SKUFormRef.value.initSKUData(categoryStore.C1Id, categoryStore.C2Id, row)
}

// 子组件SPUForm回调: 改变场景
const changeScene = (res: any) => {
  scene.value = res.scene
  if (res.returnFirstPage) {
    // 添加回到首页
    getHasSPU()
  } else {
    // 更新保留当前页
    getHasSPU(pageNum.value)
  }
}

// 获取已有SPU
const getHasSPU = async (page = 1) => {
  pageNum.value = page
  // 获取已有SPU
  const res: HasSpuResponseData = await reqHasSpu(
    pageNum.value,
    pageSize.value,
    categoryStore.C3Id,
  )
  if (res.code === 200) {
    records.value = res.data.records
    total.value = res.data.total
  }
}

// 改变每页显示数
const changeSize = (size: number) => {
  pageSize.value = size
  getHasSPU()
}

watch(
  () => categoryStore.C3Id,
  () => {
    if (!categoryStore.C3Id) return
    getHasSPU()
  },
)
</script>

<style scoped></style>
