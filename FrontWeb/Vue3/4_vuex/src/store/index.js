import Vue from "vue";
import Vuex from "vuex";
import axios from 'axios'
Vue.use(Vuex);

const countOptions = {
  namespaced: true,
  actions: {
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
  },

  mutations: {
    ADD(state, value) {
      console.log("mutations中的`ADD`被调用了");
      state.sum += value;
    },
    SUB(state, value) {
      console.log("mutations中的`SUB`被调用了");
      state.sum -= value;
    },
  },

  state: {
    sum: 0,
    studentName: "张三",
    age: 18,
  },

  getters: {
    tenTimesSum(state) {
      return state.sum * 10;
    },
  },
};

const personOptions = {
  namespaced: true, // 开启命名空间
  actions: {
    add_person(context, personObj) {
      if (!personObj.name.trim()) {
        alert("输入的名字不能为空");
        return;
      }
      context.commit("ADD_PERSON", personObj);
    },
    show_words(context) {
      axios.get("https://v1.hitokoto.cn/?c=f&encode=text").then(
        (response) => {
          context.commit("SHOW_WORDS", response.data);
        },
        (error) => {
          alert(error.message);
          context.commit("SHOW_WORDS", "");
        }
      );
    },
  },

  mutations: {
    // 用于更新personList数组
    ADD_PERSON(state, personObj) {
      state.personList.unshift(personObj);
    },

    DELETE_PERSON(state, pid) {
      state.personList = state.personList.filter((p) => p.id !== pid);
    },
    SHOW_WORDS(state, words) {
      state.words = words;
    },
  },

  state: {
    personList: [
      // 用于存储人员信息的数组
      { id: "001", name: "张三" },
      { id: "002", name: "李四" },
      { id: "003", name: "王五" },
    ],
    words: "",
  },

  getters: {
    firstPersonName(state) {
      return state.personList[0].name;
    },
  },
};

export default new Vuex.Store({
  modules: {
    myCount: countOptions,
    myPerson: personOptions,
  },
});
