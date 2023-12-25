<template>
  <el-icon @click="changeIcon">
    <component :is="LayoutSettingStore.fold ? 'Fold' : 'Expand'"></component>
  </el-icon>
  <!-- 顶部左侧面包屑 -->
  <el-breadcrumb separator-icon="ArrowRight">
    <el-breadcrumb-item>权限管理</el-breadcrumb-item>
    <el-breadcrumb-item>用户管理</el-breadcrumb-item>
  </el-breadcrumb>
</template>

<script setup lang="ts" name="Breadcrumb">
import useLayoutSettingStore from '@/store/modules/setting'
let LayoutSettingStore = useLayoutSettingStore()
const changeIcon = () => {
  LayoutSettingStore.fold = !LayoutSettingStore.fold
}
</script>

<style scoped lang="scss">
.el-icon {
  margin-right: 10px;
}
.el-breadcrumb {
  font-size: 18px;
  font-weight: 400;
}
</style>
