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
import { ref, reactive, toRefs, toRaw, markRaw } from 'vue';
export default {
    name: 'Count',
    setup() {
        const sum = ref(0)
        const person = reactive({   // 只有第一层属性不可修改
            name: '张三',
            age: 18,
            job: {
                j1: {
                    salary: 10000,
                }
            }
        })
        const p1 = toRaw(person)
        const p2 = reactive(p1)
        console.log(p1, p2)

        person.pets = {
            dog: '小黑',
            cat: '小花',
        }
        person.school = markRaw({
            name: 'Middle School',
            address: 'HangZhou',
        })
        console.log(person)

        return { ...toRefs(person), sum, }
    },
}
</script>

<style></style>