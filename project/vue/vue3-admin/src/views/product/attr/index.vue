<template>
  <div>
    <!-- 三级分类组件 -->
    <Category />
    <!-- 平台属性表格展示 -->
    <el-card style="margin: 10px 0px">
      <!-- Card头部: 添加品牌按钮 -->
      <template #header>
        <div class="clearfix">
          <el-button
            type="primary"
            icon="Plus"
            :disabled="categoryStore.C3Id ? false : true"
          >
            添加平台属性
          </el-button>
        </div>
      </template>
      <!-- 属性表格 -->
      <el-table border :data="attrArr">
        <el-table-column
          label="序号"
          type="index"
          align="center"
          width="60px"
        />
        <el-table-column
          label="属性名称"
          width="120px"
          prop="attrName"
        ></el-table-column>
        <el-table-column label="属性值名称">
          <template v-slot="{ row }">
            <el-tag
              v-for="(item, index) in row.attrValueList"
              :key="index"
              style="margin: 5px 5px"
              disable-transitions
            >
              {{ item.valueName }}
            </el-tag>
          </template>
        </el-table-column>
        <el-table-column label="操作" align="center" width="120px">
          <template v-slot="{ row }">
            <el-button type="warning" size="small" icon="Edit"></el-button>
            <el-popconfirm
              :title="`确认删除${row.tmName}?`"
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
    </el-card>
  </div>
</template>

<script setup lang="ts" name="Attr">
import { watch, ref } from 'vue'
import useCategoryStore from '@/store/modules/category'
import { reqAttr } from '@/api/product_api/attr'
import type { AttrList } from '@/api/product_api/attr/type'
import { ElMessage } from 'element-plus'
let categoryStore = useCategoryStore()
let attrArr = ref<AttrList>([])

const getAttr = async () => {
  const { C1Id, C2Id, C3Id } = categoryStore
  const res = await reqAttr(C1Id, C2Id, C3Id)
  if (res.code === 200) {
    attrArr.value = res.data
  } else {
    ElMessage.error('获取平台属性失败')
  }
}

watch(
  () => categoryStore.C3Id,
  () => {
    attrArr.value = []
    if (!categoryStore.C3Id) return
    getAttr()
  },
)
</script>

<style scoped></style>
