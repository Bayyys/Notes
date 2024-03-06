<template>
    <div>
        <h1>name: {{ name }}</h1>
        <h2>age: {{ age }}</h2>
        <h2>salary: {{ job.j1.salary }}</h2>
        <h2>hobby:</h2>
        <ol>
            <li v-for="(item, index) in hobby" :key="index"> {{ item }}</li>
        </ol>
        <button @click="name += '~'">修改姓名</button>
        <button @click="age++">修改年龄</button>
        <button @click="job.j1.salary += 1000">修改薪水</button>
    </div>
</template>

<script>
import { reactive, toRefs } from 'vue';
export default {
    name: 'Count',
    setup() {
        const person = reactive({
            name: '张三',
            age: 24,
            job: {
                j1: {
                    salary: 10000,
                }
            },
            hobby: ['吃饭', '睡觉', '打豆豆']
        })

        return {
            ...toRefs(person)
        }
    },
}
</script>

<style></style>