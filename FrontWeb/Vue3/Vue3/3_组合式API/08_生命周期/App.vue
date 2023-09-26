<template>
  <div>
    <h1>{{ msg }}</h1>
    <hr>
    <Count v-if="isShow"></Count>
    <button @click="changeShow">changeShow</button>
  </div>
</template>

<script>
import { ref, reactive } from 'vue'
import Count from './components/Count.vue'
export default {
  name: 'App',
  components: { Count },
  setup() {
    const msg = ref("hello world")
    const isShow = ref(true)
    function changeShow() {
      isShow.value = !isShow.value
    }

    return { msg, isShow, changeShow }
  }
}
</script>

<style></style>