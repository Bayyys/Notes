<template>
  <div>
    <h1>{{ msg }}</h1>
    <button @click="changeShow">changeShow</button>
    <hr>
    <Count v-if="isShow"></Count>
  </div>
</template>

<script>
import { ref } from 'vue'
import Count from './components/Count.vue'
export default {
  name: 'App',
  components: { Count },
  setup() {
    const msg = ref("Hello world!")
    const isShow = ref(true)
    function changeShow() {
      isShow.value = !isShow.value
    }

    return { msg, isShow, changeShow }
  }
}
</script>

<style></style>