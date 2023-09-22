<template>
    <div class="student">
        <h2>学生姓名: {{ name }}</h2>
        <h2>学生性别: {{ sex }}</h2>
        <button @click="sendMsg">向学校发送消息</button>
    </div>
</template>

<script>
import pubsub from 'pubsub-js'
export default {
    name: 'Student',
    data() {
        return {
            name: '张三',
            sex: '男',
        }
    },
    methods: {
        sendMsg() {
            // this.$bus.$emit('sayHello', this.name);
            pubsub.publish('sayHello', this.name);
        }
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