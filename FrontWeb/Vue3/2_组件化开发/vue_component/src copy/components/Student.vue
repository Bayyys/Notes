<template>
    <div class="myStyle">
        <h2>name: {{ name }}</h2>
        <h2>sex: {{ sex }}</h2>
    </div>
</template>

<script>

export default {
    name: 'Student',
    data() {
        return {
            name: '张三',
            sex: '男',
        }
    },
}

</script>

<style scoped>
.myStyle {
    background-color: olivedrab;
}
</style>