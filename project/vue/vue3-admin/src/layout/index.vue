<template>
  <div class="layout_container">
    <!-- 左侧菜单 -->
    <div class="layout_slider">
      <Logo />
      <!-- 展示菜单 -->
      <el-scrollbar class="scrollbar">
        <el-menu
          :collapse="LayoutSettingStore.fold"
          background-color="#001529"
          text-color="white"
          :default-active="$route.path"
        >
          <!-- 动态菜单项 -->
          <Menu :menuList="userStore.menuRoutes"></Menu>
        </el-menu>
      </el-scrollbar>
    </div>
    <!-- 顶部导航 -->
    <div class="layout_tabbar" :class="{ fold: LayoutSettingStore.fold }">
      <Tabbar></Tabbar>
    </div>
    <!-- 内容展示 -->
    <div class="layout_main" :class="{ fold: LayoutSettingStore.fold }">
      <Main></Main>
    </div>
  </div>
</template>

<script setup lang="ts" name="Layout">
import { useRoute } from 'vue-router'
import Logo from './logo/index.vue'
import Menu from './menu/index.vue'
import Main from './mainwin/index.vue'
import Tabbar from './tabbaar/index.vue'
import useUserState from '@/store/modules/user'
import useLayoutSettingStore from '@/store/modules/setting'

const userStore = useUserState()
const LayoutSettingStore = useLayoutSettingStore()
const $route = useRoute()
</script>

<style scoped lang="scss">
.layout_container {
  width: 100%;
  height: 100vh;
  background: white;
  .layout_slider {
    width: $base-menu-width;
    height: 100vh;
    background: $base-menu-bg;
    transition: all 0.3s;
    .scrollbar {
      width: 100%;
      height: calc(100vh - #{$base-logo-height});
      color: white;
    }
  }
  .layout_tabbar {
    position: fixed;
    top: 0;
    left: $base-menu-width;
    width: calc(100% - #{$base-menu-width});
    height: $base-tabbar-height;
    transition: all 0.3s;
    &.fold {
      left: $base-menu-min-width;
      width: calc(100vw - #{$base-menu-min-width});
    }
  }
  .layout_main {
    position: absolute;
    top: $base-tabbar-height;
    left: $base-menu-width;
    padding: 20px;
    width: calc(100% - #{$base-menu-width});
    height: calc(100vh - #{$base-tabbar-height});
    background: $base-main-bg;
    overflow: auto;
    transition: all 0.3s;
    &.fold {
      left: $base-menu-min-width;
      width: calc(100vw - #{$base-menu-min-width});
    }
  }
}
</style>
