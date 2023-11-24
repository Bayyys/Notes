<template>
  <div class="son">
    <h3 style="font-size: 30px;">我是子组件:曹植, money: {{ money }}</h3>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
let money = ref(666);
const fly = () => {
  console.log('我可以飞');
}
// 组件内部数据对外关闭的，别人不能访问
// 如果想让外部访问需要通过defineExpose方法对外暴露
defineExpose({
  money,
  fly
})
</script>

<style scoped>
.son {
  width: 50%;
  height: 100px;
  background: cyan;
}
</style>