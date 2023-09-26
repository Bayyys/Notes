<template>
    <div>
        <h1>name: {{ name }}</h1>
        <h2>age: {{ age }}</h2>
        <h2>salary: {{ job.j1.salary }}</h2>
        <button @click="name += '~'">修改姓名</button>
        <button @click="age++">修改年龄</button>
        <button @click="job.j1.salary += 1000; console.log(job.j1.salary)">修改薪水</button>
        <h1>sum: {{ sum }}</h1>
        <h1>count.x.y: {{ count.x.y }}</h1>
        <button @click="sum++">sum++</button>
        <button @click="count.x.y++">count.x.y++</button>
    </div>
</template>

<script>
import { reactive, toRefs, shallowRef, shallowReactive } from 'vue';
export default {
    name: 'Count',
    setup() {
        const person = shallowReactive({
            name: '张三',
            age: 18,
            job: {
                j1: {
                    salary: 10000,
                }
            }
        })
        const sum = shallowRef(0)
        const count = shallowRef({
            x: {
                y: 1
            }
        })
        return { ...toRefs(person), sum, count }
    },
}
</script>

<style></style>