<template>
  <template v-for="item in menuList" :key="item.path">
    <el-menu-item v-if="!item.children" :index="item.path">
      <template #title>
        <p>图标</p>
        &nbsp; &nbsp;
        <span>{{ item.meta.title }}</span>
      </template>
    </el-menu-item>
    <el-menu-item
      v-if="item.children && item.children.length === 1"
      :index="item.children[0].path"
    >
      <template #title>
        <span>{{ item.meta.title }}</span>
      </template>
    </el-menu-item>
  </template>
</template>

<script setup lang="ts">
defineProps(['menuList'])
</script>

<style scoped></style>
