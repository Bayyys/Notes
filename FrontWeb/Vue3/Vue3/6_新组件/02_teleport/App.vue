<template>
  <div class="app">
    <h1>App Component</h1>
    <hr>
    <Child></Child>
  </div>
</template>

<script>
import Child from './components/Child.vue'
export default {
  name: 'App',
  components: { Child },
}
</script>

<style>
.app {
  background-color: gray;
  padding: 10px;
}
</style>