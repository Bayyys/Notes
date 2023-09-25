<template>
    <div class="student">
        <h2>学生姓名: {{ name }}</h2>
        <h2>学生性别: {{ sex }}</h2>
        <button @click="giveStudentName">传递学生姓名</button>
        <button @click="unbind">解绑事件</button>
    </div>
</template>

<script>

export default {
    name: 'Student',
    data() {
        return {
            name: '张三',
            sex: '男',
        }
    },
    methods: {
        giveStudentName() {
            this.$emit('getStudentName', this.name)
        },
    }
}

</script>

<style scoped>
.student {
    background-color: olivedrab;
    padding: 5px;
    margin-top: 5px;
}
</style>