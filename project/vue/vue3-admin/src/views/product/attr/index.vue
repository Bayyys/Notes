<template>
  <div>
    <!-- 三级分类组件 -->
    <Category :scene="scene" />
    <!-- 平台属性表格展示 -->
    <el-card style="margin: 10px 0px">
      <!-- Card头部: 添加品牌按钮 -->
      <template #header>
        <div class="clearfix">
          <div v-if="scene === 0">
            <el-button
              type="primary"
              icon="Plus"
              :disabled="categoryStore.C3Id ? false : true"
              @click="addAttr"
            >
              添加平台属性
            </el-button>
          </div>
          <div v-else>
            <span>添加平台属性</span>
          </div>
        </div>
      </template>
      <div v-if="scene === 0">
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
              <el-button
                type="warning"
                size="small"
                icon="Edit"
                @click="addAttr"
              ></el-button>
              <el-popconfirm
                :title="`确认删除${row.tmName}?`"
                icon="Delete"
                icon-color="red"
              >
                <template #reference>
                  <el-button
                    size="small"
                    type="danger"
                    icon="Delete"
                  ></el-button>
                </template>
              </el-popconfirm>
            </template>
          </el-table-column>
        </el-table>
      </div>
      <div v-else>
        <el-form :inline="true">
          <el-form-item label="属性名称">
            <el-input placeholder="请输入属性名称"></el-input>
          </el-form-item>
        </el-form>
        <el-button type="primary" size="default" icon="Plus" @click="cancel">
          添加属性值
        </el-button>
        <el-button size="default" @click="cancel">取消</el-button>
        <el-table style="margin: 10px 0px; width: 100%" border>
          <el-table-column type="index" label="序号" align="center" />
          <el-table-column label="属性值名称" align="center" />
          <el-table-column label="属性值操作" align="center" />
        </el-table>
        <el-button type="primary" size="default">保存</el-button>
        <el-button size="default" @click="cancel">取消</el-button>
      </div>
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
let scene = ref<number>(0)

const getAttr = async () => {
  const { C1Id, C2Id, C3Id } = categoryStore
  const res = await reqAttr(C1Id, C2Id, C3Id)
  if (res.code === 200) {
    attrArr.value = res.data
  } else {
    ElMessage.error('获取平台属性失败')
  }
}

const addAttr = () => {
  scene.value = 1
}

const cancel = () => {
  scene.value = 0
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
