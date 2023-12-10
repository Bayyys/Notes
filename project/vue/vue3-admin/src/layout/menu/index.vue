<template>
  <template v-for="item in menuList" :key="item.path">
    <!-- 没有子路由 -->
    <template v-if="!item.children">
      <el-menu-item v-if="!item.meta.hidden" :index="item.path">
        <template #title>
          <span>{{ item.meta.title }}</span>
        </template>
      </el-menu-item>
    </template>
    <!-- 单个子路由 -->
    <template v-if="item.children && item.children.length == 1">
      <el-menu-item
        index="item.children[0].path"
        v-if="!item.children[0].meta.hidden"
      >
        <template #title>
          <span>标题</span>
          <span>{{ item.children[0].meta.title }}</span>
        </template>
      </el-menu-item>
    </template>
    <!-- 多个子路由 -->
    <el-sub-menu
      :index="item.path"
      v-if="item.children && item.children.length >= 2"
    >
      <template #title>
        <span>{{ item.meta.title }}</span>
      </template>
      <NewMenu :menuList="item.children"></NewMenu>
    </el-sub-menu>
  </template>
</template>

<script setup lang="ts">
defineProps(['menuList'])
</script>
<script lang="ts">
export default {
  name: 'NewMenu',
}
</script>

<style scoped></style>
