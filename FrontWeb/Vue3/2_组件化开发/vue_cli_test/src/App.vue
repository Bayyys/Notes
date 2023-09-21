<template>
    <div>
        <img src="./assets/logo.png" alt="logo">
        <Teacher></Teacher>
        <Student></Student>
    </div>
</template>

<script>
// 引入组件
import Teacher from './components/Teacher'
import Student from './components/Student'
export default {
    name: 'App',
    components: {
        Teacher,
        Student
    },
}
</script>