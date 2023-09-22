<template>
    <div class="app">
        <h1>你好 {{ msg }}</h1>
        <!-- props 父子传递实现 -->
        <School :getSchoolName="getSchoolName"></School>
        <hr>
        <Student v-on:getStudentName="getStudentName"></Student>
        <!-- 简写形式 -->
        <Student @getStudentName="getStudentName"></Student>
        <!-- refs 使用 -->
        <!-- <Student ref="student"/> -->
    </div>
</template>

<script>
// 引入组件
import School from './components/School.vue'
import Student from './components/Student.vue';


export default {
    name: 'App',
    components: {
        School, Student
    },
    data() {
        return {
            msg: 'Vue3'
        }
    },
    methods: {
        getSchoolName(name) {
            this.msg += name
        },
        getStudentName(name, ...params) {
            console.log(name, params)
            this.msg += name
        }
    },
}
</script>

<style scoped>
.app {
    background-color: gray;
    padding: 10px;
}
</style>