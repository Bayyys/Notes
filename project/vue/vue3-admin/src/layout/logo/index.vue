<template>
  <div class="logo" v-if="setting.logoShown">
    <img :src="setting.logo" alt="" />
    <p>{{ setting.title }}</p>
  </div>
</template>

<script setup lang="ts" name="Logo">
import setting from '@/setting'
</script>

<style scoped lang="scss">
.logo {
  width: 100%;
  height: $base-logo-height;
  color: white;
  display: flex;
  align-items: center;
  padding: 15px;
  img {
    width: 40px;
    height: 40px;
  }
  p {
    font-size: $base-logo-font-size;
    margin-left: 20px;
  }
}
</style>
