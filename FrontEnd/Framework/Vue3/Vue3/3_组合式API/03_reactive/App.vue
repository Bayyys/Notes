<template>
  <div>
    <h1>{{ msg }}</h1>
    <h1>name: {{ name }}</h1>
    <h2>studentName: {{ student.name }}</h2>
    <h2>studentAge: {{ student.age }}</h2>
    <h2>a-b-c: {{ student.a.b.c }}</h2>
    <h2 v-for="(item, index) in hobby" :key="index">{{ item }}</h2>
    <button @click="changeName">点击</button>
  </div>
</template>

<script>
import { ref, reactive } from 'vue'
export default {
  name: 'App',
  setup() {
    const name = ref("张三")
    const msg = ref("hello world")
    const student = reactive({
      name: "bayyy",
      age: 25,
      a: {
        b: {
          c: 100
        }
      }
    })
    const hobby = reactive(['吃饭', '睡觉', '打豆豆'])

    // 常用写法
    let person = reactive({
      name: "bay",
      age: 25,
      hobby: ['吃饭', '睡觉', '打豆豆'],
      a: {
        b: {
          c: 100
        }
      }
    })

    function changeName() {
      name.value = "李四"
      student.name = 'BAY'
      student.age = 30
      student.a.b.c = 200
      hobby[0] = '吃'
    }

    return { name, msg, student, hobby, person, changeName }
  }
}
</script>

<style></style>