<template>
  <div class="app">
    <Category title="美食" :listData="foods">
      <img src="https://s3.ax1x.com/2021/01/16/srJlq0.jpg" alt="">
    </Category>
    <Category title="游戏" :listData="games">
      <ul>
        <li v-for="(g, index) in games" :key="index">
          {{ g }}
        </li>
      </ul>
    </Category>
    <Category title="电影" :listData="films">
      <video src="https://www.runoob.com/try/demo_source/movie.mp4" controls></video>
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
      foods: ['蛋糕', '饼干', '巧克力', '薯片'],
      games: ['王者荣耀', '英雄联盟', '绝地求生', '穿越火线'],
      films: ['战狼', '红海行动', '流浪地球', '我不是药神'],
    }
  }
}
</script>

<style>
.app {
  display: flex;
}
</style>