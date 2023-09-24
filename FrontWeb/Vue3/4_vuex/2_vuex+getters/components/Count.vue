<template>
    <div>
        <h1>当前求和为: {{ $store.state.sum }}</h1>
        <h1>当前数值x10为: {{ $store.getters.tenTimesSum }}</h1>
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
export default {
    name: 'Count',
    data() {
        return {
            n: 1,   // 选择的数字
        }
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
    }
}
</script>

<style></style>