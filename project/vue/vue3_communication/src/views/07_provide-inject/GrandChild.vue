<template>
  <div class="child1">
    <h1>孙子组件</h1>
    <p>{{ car }}</p>
    <button @click="updateCar">换车</button>
  </div>
</template>

<script setup lang="ts">
import { inject } from 'vue';
// 注入祖先组件提供数据
// 需要参数:即为祖先提供数据的key
let car: any = inject('TOKEN');
const updateCar = () => {
  car.value = car.value === '法拉利' ? '兰博基尼' : '法拉利';
}
</script>

<style scoped>
.child1 {
  width: 50vw;
  height: 200px;
  background: red;
}
</style>