// 该文件用于创建Vuex中最为核心的store
import Vue from "vue";
// 引入Vuex
import Vuex from "vuex";
// 应用Vuex插件
Vue.use(Vuex);

// 准备actions——用于响应组件中的动作
const actions = {
  // add(context, value) {
  //   // context: store对象具有相同属性和方法的对象
  //   console.log("actions中的`add`被调用了");
  //   context.commit("ADD", value);
  // },
  // sub(context, value) {
  //   context.commit("SUB", value);
  // },
  addIfOdd(context, value) {
    console.log("actions中的`addIfOdd`被调用了");
    if (context.state.sum % 2) {
      context.commit("ADD", value);
    }
  },
  addWait(context, value) {
    console.log("actions中的`addWait`被调用了");
    setTimeout(() => {
      context.commit("ADD", value);
    }, 500);
  },
};
// 准备mutations——用于操作数据（state）
const mutations = {
  // 一般使用大写, 用来区分actions和mutations
  ADD(state, value) {
    console.log("mutations中的`ADD`被调用了");
    state.sum += value;
  },
  SUB(state, value) {
    console.log("mutations中的`SUB`被调用了");
    state.sum -= value;
  },
};
// 准备state——用于存储数据
const state = {
  sum: 0, // 当前的和
};

const getters = {
  tenTimesSum(state) {
    return state.sum * 10;
  },
};

// 创建并暴露store
export default new Vuex.Store({
  actions,
  mutations,
  state,
  getters,
});
