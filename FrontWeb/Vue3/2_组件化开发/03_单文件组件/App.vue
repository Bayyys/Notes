<template>
    <div>
        <Teacher></Teacher>
        <Student></Student>
    </div>
</template>

<script>
// 引入组件
import Teacher from './Teacher'
import Student from './Student'
export default {
    name: 'App',
    components: {
        Teacher,
        Student
    },
}
</script>