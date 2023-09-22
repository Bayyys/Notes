<template>
    <div class="school">
        <h2>学校姓名: {{ name }}</h2>
        <h2>学校地址: {{ address }}</h2>
        <button @click="unsub">取消订阅</button>
    </div>
</template>

<script>
import pubsub from 'pubsub-js';

export default {
    name: 'School',
    props: ["getSchoolName"],
    data() {
        return {
            name: 'Middle School',
            address: 'Beijing'
        }
    },
    methods: {
        unsub() {
            pubsub.unsubscribe('sayHello');
        }
    },
    mounted() {
        // this.$bus.$on('sayHello', (name) => {
        //     console.log('School Componentt received: ' + name);
        // });
        this.pubId = pubsub.subscribe('sayHello', (msgName, msg) => {
            console.log(this)
            console.log('School Componentt received: ' + msg);
        });
    },
    beforeDestroy() {
        // this.$bus.$off('sayHello');
        pubsub.unsubscribe(this.pubId);
    }
}
</script>

<style scoped>
.school {
    background-color: orange;
    padding: 5px;
    margin-top: 5px;
}
</style>