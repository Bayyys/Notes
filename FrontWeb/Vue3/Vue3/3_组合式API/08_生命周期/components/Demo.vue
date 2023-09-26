<template>
    <div>
        <h1>个人信息</h1>
        姓: <input type="text" v-model="person.firstName" />
        名: <input type="text" v-model="person.lastName" />
        年龄: <input type="number" v-model="person.age" />
        <hr>
        完整姓名: {{ person.fullName }}
    </div>
</template>

<script>
import { ref, reactive, computed, watch } from 'vue'
export default {
    name: 'Demo',
    setup(props, context) {
        const person = reactive({
            firstName: '张',
            lastName: '三',
            age: 18
        })

        person.fullName = computed(() => {
            return person.firstName + person.lastName
        })

        return { person }
    }
}
</script>

<style></style>