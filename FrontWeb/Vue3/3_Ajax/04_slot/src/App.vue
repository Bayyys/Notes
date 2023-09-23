<template>
  <div class="app">
    <Category title="游戏">
      <template scope="scopeData">
        <ul>
          <li v-for="(item, index) in scopeData.games" :key="index"> {{ item }} </li>
        </ul>
      </template>
    </Category>

    <Category title="游戏">
      <template scope="{games}">
        <ol>
          <li v-for="(item, index) in games" :key="index"> {{ item }} </li>
        </ol>
      </template>
    </Category>

    <Category title="游戏">
      <template scope="scopeData">
        <h4 v-for="(item, index) in scopeData.games" :key="index"> {{ item }} </h4>
      </template>
    </Category>
  </div>
</template>

<script>
import Category from './components/Category.vue';
export default {
  name: 'App',
  components: { Category },
  data() {
    return {
      msg: 'Hello World!',
    }
  }
}
</script>

<style>
.app {
  display: flex;
}

.foot {
  display: flex;
  justify-content: space-around;
}

h4 {
  text-align: center;
}
</style>