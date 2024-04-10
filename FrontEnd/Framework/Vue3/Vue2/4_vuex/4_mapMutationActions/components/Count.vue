<template>
    <div>
        <h1>当前求和为: {{ sum }}</h1> <!-- {{ $store.state.sum }} -->
        <h1>当前数值x10为: {{ tenTimesSum }}</h1> <!-- $store.getters.tenTimesSum -->
        <h3>我是 {{ studentName }}, 现在 {{ age }} 岁</h3> <!-- {{ $store.state.studentName }}, {{ $store.state.age }} -->
        <select v-model.number="n">
            <option value="1">1</option>
            <option value="2">2</option>
            <option value="3">3</option>
        </select> <br>
        <button @click="increment(n)">add</button>
        <button @click="decrement(n)">sub</button>
        <button @click="incOdd(n)">add if odd</button>
        <button @click="incWait(n)">add wait</button>
    </div>
</template>

<script>
// mapState: 用于简化vuex中state的使用, 用于将state映射到计算属性中
import { mapState, mapGetters, mapMutations, mapActions } from 'vuex'
export default {
    name: 'Count',
    data() {
        return {
            n: 1,   // 选择的数字
        }
    },
    computed: {
        ...mapState(['sum', 'studentName', 'age']),
        ...mapGetters(['tenTimesSum']),
    },
    methods: {
        // ...mapActions(['addIfOdd', 'addWait']), // 数组写法
        ...mapMutations({
            increment: 'ADD',
            decrement: 'SUB',
        }),
        /* 默认生成的函数如下， 自带一个传入参数 */
        // increment(value) {
        //     this.$store.commit('ADD', value)
        // },

        // ...mapActions(['addIfOdd', 'addWait']), // 数组写法
        ...mapActions({
            incOdd: 'addIfOdd',
            incWait: 'addWait',
        }),

    },
}
</script>

<style></style>