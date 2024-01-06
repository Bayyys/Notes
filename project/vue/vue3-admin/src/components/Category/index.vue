<template>
  <div>
    <el-card>
      <el-form ref="formRef" label-width="auto" inline>
        <el-form-item label="一级分类">
          <el-select placeholder="请选择" v-model="c1Id">
            <el-option
              v-for="c1 in c1Arr"
              :key="c1.id"
              :label="c1.name"
              :value="c1.id"
            />
          </el-select>
        </el-form-item>
        <el-form-item label="二级分类">
          <el-select placeholder="请选择">
            <el-option label="Options1" value="1" />
            <el-option label="Options2" value="2" />
          </el-select>
        </el-form-item>
        <el-form-item label="三级分类">
          <el-select placeholder="请选择">
            <el-option label="Options1" value="1" />
            <el-option label="Options2" value="2" />
          </el-select>
        </el-form-item>
      </el-form>
    </el-card>
  </div>
</template>

<script setup lang="ts" name="Category">
import { reqC1 } from '@/api/product_api/attr'
import { onMounted, ref } from 'vue'
let c1Arr = ref<any>()
let c1Id = ref<number | string>('')
// 获取一级分类列表
const getC1 = async () => {
  const res = await reqC1()
  if (res.code === 200) {
    c1Arr.value = res.data
  }
}

onMounted(() => {
  getC1()
})
</script>

<style scoped></style>
