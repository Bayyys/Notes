<template>
    <div>
        <h1>当前求和为: {{ sum }}</h1> <!-- {{ $store.state.sum }} -->
        <h1>当前数值x10为: {{ tenTimesSum }}</h1> <!-- $store.getters.tenTimesSum -->
        <h3>我是 {{ studentName }}, 现在 {{ age }} 岁</h3> <!-- {{ $store.state.studentName }}, {{ $store.state.age }} -->
        <h3 style="color: red;">Person Component 总人数: {{ personList.length }}</h3>
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
import { mapState, mapGetters, mapMutations, mapActions } from 'vuex'
export default {
    name: 'Count',
    data() {
        return {
            n: 1,   // 选择的数字
        }
    },
    computed: {
        ...mapState('myCount', ['sum', 'studentName', 'age']),
        ...mapState('myPerson', ['personList']),
        ...mapGetters('myCount', ['tenTimesSum']),
    },
    methods: {
        ...mapMutations('myCount', {
            increment: 'ADD',
            decrement: 'SUB',
        }),
        ...mapActions('myCount', {
            incOdd: 'addIfOdd',
            incWait: 'addWait',
        }),

    },
}
</script>

<style></style>