<template>
    <div>
        <h2>当前求和为: {{ sum }}</h2>
        <button @click="sum++">add</button>
        <button @click="person.name = '李四'">改变姓名</button>
        <button @click="person.age = 20">改变年龄</button>
        <button @click="person.pets.cat='miao~'">改变小猫</button>
    </div>
</template>

<script>
import { ref, reactive, computed, watchEffect } from 'vue';
export default {
    name: 'Count',
    setup() {
        let sum = ref(0)
        let sumTimesTen = computed(() => {
            return sum.value * 10
        })

        let person = reactive({
            name: '张三',
            age: 18,
            pets: {
                cat: '小白',
                dog: '小黑'
            }
        })

        watchEffect(() => {
            let s = sum.value
            let p = person.name
            console.log('watchEffect配置的回调执行了')
        })

        return { sum, sumTimesTen, person }
    },
}
</script>

<style></style>