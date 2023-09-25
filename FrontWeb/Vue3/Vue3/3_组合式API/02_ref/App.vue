<template>
  <div>
    <h1>{{ msg }}</h1>
    <h2>name: {{ name }}</h2>
    <h2>age: {{ age }}</h2>
    <h2>schoolName: {{ school.name }}</h2>
    <h2>schoolAdress: {{ school.address }}</h2>
    <button @click="changeName">点击</button>
  </div>
</template>

<script>
import { ref, reactive } from 'vue'
export default {
  name: 'App',
  setup() {
    const name = ref("张三")
    const age = ref(18)
    const msg = ref("hello world")
    const school = ref({
      name: "Middle School",
      address: "Beijing"
    })


    function changeName() {
      console.log(name)
      console.log(school)
      name.value = "李四"
      age.value = 20
      school.value.name = 'High School'
      school.value.address = 'Shanghai'
    }

    return { name, age, msg, school, changeName }
  }
}
</script>

<style></style>