<template>
  <div>
    <Category></Category>
    <el-card style="margin: 10px 0px">
      <!-- Card头部: 添加品牌按钮 -->
      <template #header>
        <div class="clearfix">
          <div>
            <el-button
              type="primary"
              icon="Plus"
              :disabled="categoryStore.C3Id ? false : true"
            >
              添加SPU
            </el-button>
          </div>
        </div>
      </template>
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
            <el-button type="primary" size="small" icon="Plus"></el-button>
            <el-button type="warning" size="small" icon="Edit"></el-button>
            <el-button type="info" size="small" icon="Location"></el-button>
            <el-popconfirm
              :title="`确认删除${row.attrName}?`"
              icon="Delete"
              icon-color="red"
            >
              <template #reference>
                <el-button size="small" type="danger" icon="Delete"></el-button>
              </template>
            </el-popconfirm>
          </template>
        </el-table-column>
      </el-table>
      <el-pagination
        v-show="categoryStore.C3Id"
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
    </el-card>
  </div>
</template>

<script setup lang="ts">
import { ref, watch } from 'vue'
import { reqHasSPU } from '@/api/product_api/spu'
import type { HasSPUResponseData, Records } from '@/api/product_api/spu/type'
import useCategoryStore from '@/store/modules/category'
let categoryStore = useCategoryStore()
let pageNum = ref<number>(1) // 默认页码
let pageSize = ref<number>(3) // 默认每页显示数
let total = ref<number>(10) // 总条数
let records = ref<Records>([]) // SPU列表

const getHasSPU = async (page = 1) => {
  pageNum.value = page
  // 获取已有SPU
  const res: HasSPUResponseData = await reqHasSPU(
    pageNum.value,
    pageSize.value,
    categoryStore.C3Id,
  )
  if (res.code === 200) {
    records.value = res.data.records
    total.value = res.data.total
  }
}

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
