<template>
    <div class="demo">
        <h2>学生姓名: {{ name }}</h2>
        <h2>学生年龄: {{ age }}</h2>
    </div>
</template>

<script>
export default {
    name: "Student",
    data() {
        return {
            name: "王五",
            age: 18
        }
    },
    methods: {
        changeName() {
            this.name = this.name === '王五' ? '赵六' : '王五'
        }
    },
}

</script>

<style>
    .demo {
        background-color: orange;
    }
</style>