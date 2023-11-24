<template>
  <div class="box">
    <h1>App</h1>
    <h1>{{ str }}</h1>
  </div>
</template>

<script setup lang="ts">
const str = 'hello world'
</script>

<style scoped lang="scss">
.box {
  width: 100vw;
  height: 400px;
  background: wheat;

  h1 {
    color: pink;
  }
}
</style>
