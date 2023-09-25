<template>
    <div class="student">
        <h2>{{ msg }}</h2>
        <h2>name: {{ name }}</h2>
        <h2>age: {{ age }}</h2>
        <h2>sex: {{ sex }}</h2>
    </div>
</template>

<script>
export default {
    name: 'Student',
    data() {
        return {
            msg: 'Hello Vue3',
        }
    },
    // 简单声明接收
    // props: ['name', 'age', 'sex']

    // 类型限制
    // props: {
    //     name: String,
    //     age: Number,
    //     sex: String,
    // }

    // 更多限制
    props: {
        name: {
            type: String,   // 类型是字符串
            required: true, // 必须项
        },
        age: {
            type: Number,   // 类型是数字
            default: 18,    // 默认值是18
        },
        sex: {
            type: String,   // 类型是字符串
            default: '男',  // 默认值是男
        },
    }
}

</script>

<style>
.student {
    background-color: orange;
}
</style>