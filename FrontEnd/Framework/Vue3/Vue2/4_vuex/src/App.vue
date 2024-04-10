<template>
  <div>
    <h1>{{ msg }}</h1>
    <hr>
    <Count></Count>
    <hr>
    <Person></Person>
  </div>
</template>

<script>
import Count from './components/Count.vue'
import Person from './components/Person.vue';
export default {
  name: 'App',
  components: { Count, Person },
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