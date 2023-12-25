<template>
  <!-- 按钮 -->
  <el-button size="default" icon="Refresh" circle></el-button>
  <el-button size="default" icon="FullScreen" circle></el-button>
  <el-button size="default" icon="Setting" circle></el-button>
  <!-- 头像 -->
  <img
    alt=""
    src="logo.png"
    style="width: 32px; height: 32px; margin: 0px 10px"
  />
  <!-- 下拉菜单 -->
  <el-dropdown>
    <span class="el-dropdown-link">
      admin
      <el-icon class="el-icon--right">
        <arrow-down />
      </el-icon>
    </span>
    <template #dropdown>
      <el-dropdown-menu>
        <el-dropdown-item>Logout</el-dropdown-item>
      </el-dropdown-menu>
    </template>
  </el-dropdown>
</template>

<script setup lang="ts" name="Setting"></script>

<style scoped lang="scss">
.el-button {
  margin-left: 10px;
}
</style>
