<template>
  <div>
    <h1>{{ msg }}</h1>
    <hr>
    <Count></Count>
  </div>
</template>

<script>
import Count from './components/Count.vue'
export default {
  name: 'App',
  components: { Count },
  data() {
    return {
      msg: 'Hello World!',
    }
  },
}
</script>

<style>
button {
  margin-left: 5px;
}
</style>