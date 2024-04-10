<template>
  <div>
    <h1>{{ msg }}</h1>
    <button @click="getStudents">获取学生信息</button>
    <button @click="getCar">获取汽车信息</button>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'App',
  data() {
    return {
      msg: 'Hello World!'
    }
  },
  methods: {
    getStudents() {
      axios.get('http://localhost:8080/5000/students').then(
        response => {
          console.log('成功了', response.data)
        },
        error => {
          console.log('失败了', error.message)
        }
      )
    },
    getCar() {
      axios.get('http://localhost:8080/5001/cars').then(
        response => {
          console.log('成功了', response.data)
        },
        error => {
          console.log('失败了', error.message)
        }
      )
    }
  }
}

</script>

<style></style>