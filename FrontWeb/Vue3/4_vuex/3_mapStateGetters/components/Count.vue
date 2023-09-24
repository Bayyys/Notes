<template>
    <div>
        <h1>当前求和为: {{ mySum }}</h1>    <!-- {{ $store.state.sum }} -->
        <h1>当前数值x10为: {{ tenTimesSum }}</h1>    <!-- $store.getters.tenTimesSum -->
        <h3>我是 {{ myStudentName }}, 现在 {{ myAge }} 岁</h3>  <!-- {{ $store.state.studentName }}, {{ $store.state.age }} -->
        <select v-model.number="n">
            <option value="1">1</option>
            <option value="2">2</option>
            <option value="3">3</option>
        </select> <br>
        <button @click="increment">add</button>
        <button @click="decrement">sub</button>
        <button @click="incOdd">add if odd</button>
        <button @click="incWait">add wait</button>
    </div>
</template>

<script>
// mapState: 用于简化vuex中state的使用, 用于将state映射到计算属性中
import { mapState, mapGetters } from 'vuex'
export default {
    name: 'Count',
    data() {
        return {
            n: 1,   // 选择的数字
        }
    },
    computed: {
        // ...mapState(['sum', 'studentName', 'age']), // mapState返回是一个对象， {} 需要使用ES6的对象展开运算符放入computed
        ...mapState({ mySum: 'sum', myStudentName: 'studentName', myAge: 'age' }),   // 对象形式重命名

        ...mapGetters(['tenTimesSum'])  //数组写法
        // ...mapGetters({ ten: 'tenTimesSum'})    // 对象写法
    },
    methods: {
        increment() {
            this.$store.commit('ADD', this.n)
        },
        decrement() {
            this.$store.commit('SUB', this.n)
        },
        incOdd() {
            this.$store.dispatch('addIfOdd', this.n)
        },
        incWait() {
            this.$store.dispatch('addWait', this.n)
        },
    },
}
</script>

<style></style>