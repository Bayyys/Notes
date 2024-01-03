<template>
  <div>
    <h1>HOME</h1>
  </div>
</template>

<script setup lang="ts">
import { onMounted } from 'vue'
import { ElNotification } from 'element-plus'
import { getTimePeriod } from '@/utils/time'
import useUserStore from '@/store/modules/user'
let userStore = useUserStore()
// 首页挂载完毕, 获取用户信息
onMounted(() => {
  userStore
    .userInfo()
    .then(() => {
      ElNotification({
        title: '登录成功',
        message: `${getTimePeriod()}好, ${userStore.username}`,
        type: 'success',
        duration: 2000,
      })
    })
    .catch(() => {
      console.log('获取用户信息失败')
    })
})
</script>

<style scoped></style>
