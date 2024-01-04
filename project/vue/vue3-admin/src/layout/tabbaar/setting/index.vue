<template>
  <!-- 按钮 -->
  <el-button
    size="default"
    icon="Refresh"
    circle
    @click="updateRefresh"
  ></el-button>
  <el-button
    size="default"
    icon="FullScreen"
    circle
    @click="fullScreen"
  ></el-button>
  <el-button size="default" icon="Setting" circle></el-button>
  <!-- 头像 -->
  <img
    alt=""
    :src="userStore.avatar"
    style="width: 32px; height: 32px; margin: 0px 10px; border-radius: 50%"
  />
  <!-- 下拉菜单 -->
  <el-dropdown>
    <span class="el-dropdown-link">
      {{ userStore.username }}
      <el-icon class="el-icon--right">
        <arrow-down />
      </el-icon>
    </span>
    <template #dropdown>
      <el-dropdown-menu>
        <el-dropdown-item @click="logout">Logout</el-dropdown-item>
      </el-dropdown-menu>
    </template>
  </el-dropdown>
</template>

<script setup lang="ts" name="Setting">
import { useRouter, useRoute } from 'vue-router'
import useLayoutSettingStore from '@/store/modules/setting'
import useUserStore from '@/store/modules/user'
import { ElNotification } from 'element-plus'
const $router = useRouter()
const $route = useRoute()
let layoutSettingStore = useLayoutSettingStore() // 侧边栏折叠状态
let userStore = useUserStore() // 用户信息
// 刷新页面
const updateRefresh = () => {
  layoutSettingStore.refresh = !layoutSettingStore.refresh
}
// 全屏
const fullScreen = () => {
  //DOM对象的一个属性：可以用来判断当前是不是全屏的模式【全屏：true，不是全屏：false】
  let full = document.fullscreenElement
  //切换成全屏
  if (!full) {
    //文档根节点的方法requestFullscreen实现全屏
    document.documentElement.requestFullscreen()
  } else {
    //退出全屏
    document.exitFullscreen()
  }
}
// 退出登录
const logout = async () => {
  // 1. 向服务器发送退出请求
  // 2. 相关数据清空
  // 3. 跳转到登录页面
  await userStore
    .userLogout()
    .then(() => {
      ElNotification({
        title: '退出成功',
        message: 'Bye Bye!',
        type: 'success',
      })
      $router.push({ path: '/login', query: { redirect: $route.path } })
    })
    .catch(() => {
      ElNotification({
        title: '失败',
        message: '退出失败',
        type: 'error',
      })
    })
}
</script>

<style scoped lang="scss">
.el-button {
  margin-left: 10px;
}
</style>
