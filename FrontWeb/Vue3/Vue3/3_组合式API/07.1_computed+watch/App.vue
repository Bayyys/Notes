<template>
  <div>
    <h1>{{ msg }}</h1>
    <Demo></Demo>
    <hr>
    <Count></Count>
  </div>
</template>

<script>
import { ref, reactive } from 'vue'
import Demo from './components/Demo.vue'
import Count from './components/Count.vue'
export default {
  name: 'App',
  components: { Demo, Count },
  setup() {
    const msg = ref("hello world")

    return { name, msg, }
  }
}
</script>

<style></style>