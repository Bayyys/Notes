<template>
    <div>
        <h1>当前求和为: {{ sum }}</h1>
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
            sum: 0, // 求和结果

        }
    },
    methods: {
        increment() {
            this.sum += this.n
        },
        decrement() {
            this.sum -= this.n
        },
        incOdd() {
            if(this.sum % 2) this.sum += this.n
        },
        incWait() {
            setTimeout(() => {
                this.sum += this.n
            }, 1000)
        },
    }
}
</script>

<style></style>