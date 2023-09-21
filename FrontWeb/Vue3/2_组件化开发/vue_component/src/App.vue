<template>
    <div>
        <h1 v-text="msg" ref="title"></h1>
        <button @click="showDOM" ref="btn">按钮</button>
        <School ref="sch"></School>
    </div>
</template>

<script>
// 引入School组件
import School from './components/School'

export default {
    name: 'App',
    components: {
        School
    },
    data() {
        return {
            msg: 'Hello Vue3'
        }
    },
    methods: {
        showDOM() {
            console.log(this)
            console.log(this.$refs.title)
            console.log(this.$refs.btn)
            console.log(this.$refs.sch)
        }
    },
}

</script>

<style>
</style>