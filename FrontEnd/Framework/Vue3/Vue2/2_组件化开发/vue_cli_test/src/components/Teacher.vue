<template>
    <div>
        <h2>老师姓名: {{ teacherName }}</h2>
        <h2>老师年龄: {{ age }}</h2>
        <button @click="changeName">changeName</button>
    </div>
</template>

<script>
export default {
    name: 'Teacher',
    data() {
        return {
            teacherName: '张三',
            age: 25
        }
    },
    methods: {
        changeName() {
            this.teacherName = this.teacherName === '李四' ? '张三' : '李四'
        }
    },
}
</script>

<style>
</style>