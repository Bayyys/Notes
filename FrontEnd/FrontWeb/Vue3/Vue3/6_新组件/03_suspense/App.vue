<template>
  <div class="app">
    <h1>App Component</h1>
    <hr>
    <Suspense>
      <template v-slot:default>
        <Child></Child>
      </template>
      <template v-slot:fallback>
        <h3>加载中....</h3>
      </template>
    </Suspense>
  </div>
</template>

<script>
// import Child from './components/Child.vue'
import { defineAsyncComponent } from 'vue';
const Child = defineAsyncComponent(() => import('./components/Child.vue'));
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