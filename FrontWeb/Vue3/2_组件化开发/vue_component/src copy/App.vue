<template>
    <div>
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
            msg: 'Hello Vue3'
        }
    },
}

</script>

<style>
</style>