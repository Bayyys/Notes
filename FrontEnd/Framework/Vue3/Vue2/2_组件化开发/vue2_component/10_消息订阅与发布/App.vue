<template>
    <div class="app">
        <h1>{{ msg }}</h1>
        <School></School>
        <hr>
        <Student></Student>
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
            msg: "Hello Vue",
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