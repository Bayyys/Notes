<template>
  <div class="son">
    <h1>我是子组件: 曹植</h1>
    <p>info: {{ props.info }}</p>
    <p>money: {{ props.money }}</p>
    <!-- props 是代理对象, 可以省略前面的名字 -->
    <p>info: {{ info }}</p>
    <p>info: {{ money }}</p>
    <button @click="updateProps">修改props数据</button>
  </div>
</template>

<script setup lang="ts">
// 需要使用到defineProps方法去接受父组件传递过来的数据
// defineProps是Vue3提供方法,不需要引入直接使用(组合式API)
let props = defineProps(['info', 'money']); // 数组|对象写法都可以
// 按钮点击的回调
const updateProps = () => {
  // props.money += 10;  // props:只读的
  console.log(props.info)
}
</script>

<style scoped>
.son {
  width: 50vw;
  height: 300px;
  background: wheat;
}
</style>