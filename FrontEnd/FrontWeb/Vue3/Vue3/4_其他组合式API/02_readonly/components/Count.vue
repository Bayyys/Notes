<template>
    <div>
        <h1>name: {{ name }}</h1>
        <h2>age: {{ age }}</h2>
        <h2>salary: {{ job.j1.salary }}</h2>
        <button @click="name += '~'">修改姓名</button>
        <button @click="age++">修改年龄</button>
        <button @click="job.j1.salary += 1000; console.log(job.j1.salary)">修改薪水</button>
        <h1>sum: {{ sum }}</h1>
        <button @click="sum++">sum++</button>
    </div>
</template>

<script>
import { ref, reactive, toRefs, readonly, shallowReadonly } from 'vue';
export default {
    name: 'Count',
    setup() {
        const sum = ref(0)
        // const person = readonly(reactive({   // 所有属性都不可修改
        const person = shallowReadonly(reactive({   // 只有第一层属性不可修改
            name: '张三',
            age: 18,
            job: {
                j1: {
                    salary: 10000,
                }
            }
        }))

        return { ...toRefs(person), sum, }
    },
}
</script>

<style></style>