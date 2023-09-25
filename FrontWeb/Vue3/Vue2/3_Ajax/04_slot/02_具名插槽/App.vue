<template>
  <div class="app">
    <Category title="美食" :listData="foods">
      <img slot="center" src="https://s3.ax1x.com/2021/01/16/srJlq0.jpg" alt="">
      <!-- slot可以追加 -->
      <a slot="footer" href="https://www.baidu.com">本地美食</a>
      <a slot="footer" href="https://www.baidu.com">异域美食</a>
    </Category>
    <Category title="游戏" :listData="games">
      <ul slot="center">
        <li v-for="(g, index) in games" :key="index">
          {{ g }}
        </li>
      </ul>
      <div slot="footer" class="foot">
        <a href="https://www.baidu.com">单机游戏</a>
        <a href="https://www.baidu.com">网络游戏</a>
      </div>
    </Category>
    <Category title="电影" :listData="films">
      <video slot="center" src="https://www.runoob.com/try/demo_source/movie.mp4" controls></video>
      <template v-slot:footer>
        <div class="foot">
          <a href="https://www.baidu.com">动作电影</a>
          <a href="https://www.baidu.com">爱情电影</a>
          <a href="https://www.baidu.com">科幻电影</a>
        </div>
        <h4>欢迎前来观影!</h4>
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

.foot {
  display: flex;
  justify-content: space-around;
}

h4 {
  text-align: center;
}
</style>