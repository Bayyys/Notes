<template>
  <div>
    <el-card>
      <el-form ref="formRef" label-width="auto" inline>
        <el-form-item label="一级分类">
          <el-select
            :disabled="scene === 1"
            placeholder="请选择"
            v-model="categoryStore.C1Id"
            @change="getC2"
          >
            <el-option
              v-for="c1 in categoryStore.C1Arr"
              :key="c1.id"
              :label="c1.name"
              :value="c1.id"
            ></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="二级分类">
          <el-select
            :disabled="scene === 1"
            placeholder="请选择"
            v-model="categoryStore.C2Id"
            @change="getC3"
          >
            <el-option
              v-for="c2 in categoryStore.C2Arr"
              :key="c2.id"
              :label="c2.name"
              :value="c2.id"
            ></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="三级分类">
          <el-select
            :disabled="scene === 1"
            placeholder="请选择"
            v-model="categoryStore.C3Id"
          >
            <el-option
              v-for="c3 in categoryStore.C3Arr"
              :key="c3.id"
              :label="c3.name"
              :value="c3.id"
            ></el-option>
          </el-select>
        </el-form-item>
      </el-form>
    </el-card>
  </div>
</template>

<script setup lang="ts" name="Category">
import { onMounted } from 'vue'
import useCategoryStore from '@/store/modules/category'
let categoryStore = useCategoryStore()
defineProps(['scene'])

const getC1 = () => {
  categoryStore.getC1()
}

const getC2 = () => {
  categoryStore.getC2()
}

const getC3 = () => {
  categoryStore.getC3()
}

// 挂载时获取分类列表
onMounted(() => {
  getC1()
})
</script>

<style scoped></style>
