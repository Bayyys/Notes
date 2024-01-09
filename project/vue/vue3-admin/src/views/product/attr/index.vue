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
                @click="updateAttr(row)"
              ></el-button>
              <el-popconfirm
                :title="`确认删除${row.attrName}?`"
                icon="Delete"
                icon-color="red"
                @confirm="deleteAttr(row.id)"
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
            <el-input
              placeholder="请输入属性名称"
              v-model="attrParams.attrName"
            ></el-input>
          </el-form-item>
        </el-form>
        <el-button
          type="primary"
          size="default"
          icon="Plus"
          @click="addAttrValue"
          :disabled="attrParams.attrName ? false : true"
        >
          添加属性值
        </el-button>
        <el-button size="default" @click="cancel">取消</el-button>
        <el-table
          :data="attrParams.attrValueList"
          style="margin: 10px 0px; width: 100%"
          border
        >
          <el-table-column type="index" label="序号" align="center" />
          <el-table-column label="属性值名称" align="center">
            <template v-slot="{ row, $index }">
              <el-input
                :ref="(vc: any) => (inputArr[$index] = vc)"
                v-if="row.flag"
                @blur="toLook(row, $index)"
                placeholder="请输入属性值名称"
                v-model="row.valueName"
              ></el-input>
              <div v-else @click="toEdit(row, $index)">{{ row.valueName }}</div>
            </template>
          </el-table-column>
          <el-table-column label="属性值操作" align="center">
            <template v-slot="{ $index }">
              <el-button
                type="warning"
                size="small"
                icon="Delete"
                @click="attrParams.attrValueList.splice($index, 1)"
              ></el-button>
            </template>
          </el-table-column>
        </el-table>
        <el-button
          type="primary"
          size="default"
          @click="save"
          :disabled="attrParams.attrValueList.length > 0 ? false : true"
        >
          保存
        </el-button>
        <el-button size="default" @click="cancel">取消</el-button>
      </div>
    </el-card>
  </div>
</template>

<script setup lang="ts" name="Attr">
import { watch, ref, reactive, nextTick, onBeforeUnmount } from 'vue'
import useCategoryStore from '@/store/modules/category'
import {
  reqAddOrUpdateAttr,
  reqAttr,
  reqDeleteAttr,
} from '@/api/product_api/attr'
import type { Attr, AttrList, AttrValue } from '@/api/product_api/attr/type'
import { ElMessage } from 'element-plus'
let categoryStore = useCategoryStore() // 三级分类仓库
let attrArr = ref<AttrList>([]) // 平台属性数组
let scene = ref<number>(0) // 场景状态
let attrParams = reactive<Attr>({
  // 平台属性参数
  attrName: '',
  attrValueList: [],
  categoryId: '',
  categoryLevel: 3,
})
let inputArr = ref<any[]>([]) // input框数组

// 获取平台属性
const getAttr = async () => {
  const { C1Id, C2Id, C3Id } = categoryStore
  const res = await reqAttr(C1Id, C2Id, C3Id)
  if (res.code === 200) {
    attrArr.value = res.data
  } else {
    ElMessage.error('获取平台属性失败')
  }
}

// 显示界面添加属性值按钮点击事件: 切换场景
const addAttr = () => {
  scene.value = 1
  Object.assign(attrParams, {
    attrName: '',
    attrValueList: [],
    categoryId: '',
  })
  attrParams.categoryId = categoryStore.C3Id
}

const updateAttr = (row: Attr) => {
  scene.value = 1
  Object.assign(attrParams, JSON.parse(JSON.stringify(row))) // 浅拷贝: 会改变原对象(使用JSON转换操作进行深拷贝)
  attrParams.categoryId = categoryStore.C3Id
}

// 保存属性值按钮点击事件
const save = async () => {
  // 保存平台属性
  const res = await reqAddOrUpdateAttr(attrParams)
  if (res.code === 200) {
    scene.value = 0 // 切换场景
    ElMessage.success(`${attrParams.id ? '修改' : '添加'}平台属性成功`) // 提示信息
    getAttr() // 重新获取平台属性
  } else {
    ElMessage.error(`${attrParams.id ? '修改' : '添加'}平台属性失败`)
  }
}

// 取消按钮点击事件
const cancel = () => {
  scene.value = 0
}

// 添加属性值按钮点击事件
const addAttrValue = () => {
  // 向数组添加一个属性值对象
  attrParams.attrValueList.push({
    valueName: '',
    flag: true,
  })
  nextTick(() => {
    inputArr.value[inputArr.value.length - 1].focus()
  })
}

const deleteAttr = async (attrId: number) => {
  // 删除平台属性
  const res = await reqDeleteAttr(attrId)
  if (res.code === 200) {
    ElMessage.success('删除平台属性成功')
    getAttr()
  } else {
    ElMessage.error('删除平台属性失败')
  }
}

// 失去焦点事件
const toLook = (row: AttrValue, $index: number) => {
  if (row.valueName.trim() === '') {
    // 名称为空
    attrParams.attrValueList.splice($index, 1)
    ElMessage.error('属性值不能为空')
    row.flag = true
    return
  }
  let repeat = attrParams.attrValueList.some(
    (item) => item.valueName === row.valueName && item !== row,
  )
  if (repeat) {
    // 属性值重复
    attrParams.attrValueList.splice($index, 1)
    ElMessage.error('属性值不能重复')
    row.flag = true
  }
  row.flag = false
}

// 点击属性值名称时，input框变为可编辑状态
const toEdit = (row: AttrValue, $index: number) => {
  // 点击属性值名称时，input框变为可编辑状态
  row.flag = true
  nextTick(() => {
    inputArr.value[$index].focus()
  })
}

watch(
  () => categoryStore.C3Id,
  () => {
    attrArr.value = []
    if (!categoryStore.C3Id) return
    getAttr()
  },
)

onBeforeUnmount(() => {
  // 仓库清空
  categoryStore.$reset()
})
</script>

<style scoped></style>
