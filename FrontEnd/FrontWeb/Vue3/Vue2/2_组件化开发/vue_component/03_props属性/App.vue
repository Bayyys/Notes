<template>
    <div>
        <Student name="张三" age="20" sex="男"></Student>
    </div>
</template>

<script>
// 引入School组件
import Student from './components/Student'

export default {
    name: 'App',
    components: {
        Student
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