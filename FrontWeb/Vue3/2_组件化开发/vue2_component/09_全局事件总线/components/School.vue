<template>
    <div class="school">
        <h2>学校姓名: {{ name }}</h2>
        <h2>学校地址: {{ address }}</h2>
    </div>
</template>

<script>
export default {
    name: 'School',
    props: ["getSchoolName"],
    data() {
        return {
            name: 'Middle School',
            address: 'Beijing'
        }
    },
    mounted() {
        this.$bus.$on('sayHello', (name) => {
            console.log('School Componentt received: ' + name);
        });
    },
    beforeDestroy() {
        // 解绑事件
        // $on 和 $off 必须成对出现！！
        this.$bus.$off('sayHello');
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