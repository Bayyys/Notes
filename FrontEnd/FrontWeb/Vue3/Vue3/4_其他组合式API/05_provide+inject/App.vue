<template>
  <div class="app">
    <h1>{{ msg }}, {{ name }} --- {{ price }}</h1>
    <hr>
    <Child></Child>
  </div>
</template>

<script>
import { ref, reactive, provide, toRefs } from 'vue'
import Child from './components/Child.vue'
export default {
  name: 'App',
  components: { Child },
  setup() {
    const msg = ref("App Component")
    const car = reactive({
      name: "SOU~",
      price: "25W"
    })
    provide('car', car)
    return { msg, ...toRefs(car) }
  }
}
</script>

<style>
.app {
  background-color: gray;
  padding: 10px;
}
</style>