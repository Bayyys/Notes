<template>
  <div>
    <h1>{{ msg }}</h1>
    <h2>name: {{ name }}</h2>
    <h2>age: {{ age }}</h2>
    <button @click="sayHello">点击</button>
  </div>
</template>

<script>
import { h } from 'vue'
export default {
  name: 'App',
  setup() {
    // 数据
    let name = "张三"
    let age = 18
    let msg = "hello world"

    // 方法
    function sayHello() {
      console.log("hello world! " + `我是${name}，今年${age}岁了!`)
    }
    return () => { return h('h1', 'Hello World!') }
  }
}
</script>

<style></style>