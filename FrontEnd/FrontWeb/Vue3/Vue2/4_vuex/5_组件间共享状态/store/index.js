// 该文件用于创建Vuex中最为核心的store
import Vue from "vue";
import Vuex from "vuex";
Vue.use(Vuex);

const actions = {
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

const mutations = {
  ADD(state, value) {
    console.log("mutations中的`ADD`被调用了");
    state.sum += value;
  },
  SUB(state, value) {
    console.log("mutations中的`SUB`被调用了");
    state.sum -= value;
  },
  // 用于更新personList数组
  ADD_PERSON(state, personObj) {
    state.personList.unshift(personObj);
  },

  DELETE_PERSON(state, pid) {
    state.personList = state.personList.filter((p) => p.id !== pid);
  }
};

const state = {
  sum: 0,
  studentName: "张三",
  age: 18,
  personList: [
    // 用于存储人员信息的数组
    { id: "001", name: "张三" },
    { id: "002", name: "李四" },
    { id: "003", name: "王五" },
  ],
};

const getters = {
  tenTimesSum(state) {
    return state.sum * 10;
  },
};

export default new Vuex.Store({
  actions,
  mutations,
  state,
  getters,
});
