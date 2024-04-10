<template>
    <div class="app">
        <h1>你好 {{ msg }}</h1>
        <School :getSchoolName="getSchoolName"></School>
        <hr>
        <Student @getStudentName="getStudentName"></Student>
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
            msg: 'Vue3',
            studentName: '',
        }
    },
    methods: {
        getSchoolName(name) {
            this.msg += name
        },
        getStudentName(name) {
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