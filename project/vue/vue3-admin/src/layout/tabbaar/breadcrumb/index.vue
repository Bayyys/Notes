<template>
  <el-icon @click="changeIcon">
    <component :is="LayoutSettingStore.fold ? 'Fold' : 'Expand'"></component>
  </el-icon>
  <!-- 顶部左侧面包屑 -->
  <el-breadcrumb separator-icon="ArrowRight">
    <el-breadcrumb-item
      v-for="(item, index) in $route.matched"
      :key="index"
      v-show="item.meta.title"
      :to="item.path"
    >
      <el-icon style="vertical-align: middle" v-if="item.meta.icon">
        <component :is="item.meta.icon"></component>
      </el-icon>
      <span>{{ item.meta.title }}</span>
    </el-breadcrumb-item>
  </el-breadcrumb>
</template>

<script setup lang="ts" name="Breadcrumb">
import { useRoute } from 'vue-router'
import useLayoutSettingStore from '@/store/modules/setting'
let LayoutSettingStore = useLayoutSettingStore() // 侧边栏折叠状态
let $route = useRoute() // 路由对象
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
