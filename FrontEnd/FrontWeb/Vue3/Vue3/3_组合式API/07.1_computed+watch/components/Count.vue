<template>
    <div>
        <h2>当前求和为: {{ sum }}</h2>
        <button @click="sum++">add</button>
        <button @click="person.name = '李四'">person</button>
    </div>
</template>

<script>
import { ref, reactive, computed, watch } from 'vue';
export default {
    name: 'Count',
    watch: {
        /* 简单写法 */
        // sum(newValue, oldValue) {
        //     console.log(newValue, oldValue)
        // }

        /* 复杂写法 */
        // sum: {
        //     immediate: true,    // 立即执行
        //     deep: true,         // 深度监听
        //     handler(newValue, oldValue) {
        //         console.log(newValue, oldValue)
        //     }
        // }
    },
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

        /* 监听ref */
        // 1) 监听单个ref
        watch(sum, (newValue, oldValue) => {
            console.log("监听 'sum', " + "new: " + newValue + ";old: " + oldValue)
        })

        // 2) 监听多个ref
        watch([sum, sumTimesTen], (newValue, oldValue) => {
            console.log("监听 'sum' 和 'sumTimesTen', " + "new: " + newValue + ", old: " + oldValue)
        })

        // 3) 监听ref并添加配置
        watch(sum, (newValue, oldValue) => {
            console.log("监听 'sum', " + "new: " + newValue + "; old: " + oldValue)
        }, {
            immediate: true,    // 立即执行
            deep: true,         // 深度监听
        })

        /* 监听reactive */
        // 1) 监听reactive定义的响应式数据
        watch(person, (newValue, oldValue) => {
            console.log("监听 'person', ", newValue, oldValue)
        }, {
            deep: false // 强制不深度监听, 设置为false也会监听到
        })

        // 2) 监听reactive定义的响应式数据并添加配置
        watch(person, (newValue, oldValue) => {
            console.log("监听 'person' + 配置 ", newValue, oldValue)
        }, {
            immediate: true,    // 立即执行
            deep: true,         // 深度监听
        })

        // 3) 监听reactive定义的响应式数据中的具体某个属性
        watch(() => person.name, (newValue, oldValue) => {
            console.log("监听 'person.name', ", newValue, oldValue)
        })

        // 4) 监听reactive定义的响应式数据中的具体某个属性并添加配置
        watch(() => person.name, (newValue, oldValue) => {
            console.log("监听 'person.name' + 配置, ", newValue, oldValue)
        }, {
            immediate: true,    // 立即执行
            deep: true,         // 深度监听
        })

        // 5) 监听reactive定义的响应式数据中的某些值
        watch([() => person.name, () => person.age], (newValue, oldValue) => {
            console.log("监听 'person.name' 和 'person.age', ", newValue, oldValue)
        })


        return { sum, sumTimesTen, person }
    },
}
</script>

<style></style>