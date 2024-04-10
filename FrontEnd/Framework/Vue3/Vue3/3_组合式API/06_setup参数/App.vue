<template>
  <div>
    <h1>{{ msg }}</h1>
    <Demo @sayHello="sayHello" msg="msg" name="name">
      <template v-slot:demo>
        <h2>Solt Input</h2>
      </template>
    </Demo>
    <button @click="say">点击</button>
  </div>
</template>

<script>
import { ref, reactive } from 'vue'
import Demo from './components/Demo.vue'
export default {
  name: 'App',
  components: { Demo },
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

    function sayHello(value) {
      msg.value = `Demo 触发了 sayHello(), 传参为 ${value}`
    }

    return { name, msg, student, hobby, person, changeName, sayHello }
  }
}
</script>

<style></style>