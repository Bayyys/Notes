<template>
    <div>
        <h1>Banner Info: {{ msg }}</h1>
    </div>
</template>

<script>
export default {
    name: 'Banner',
    data() {
        return {
            msg: 'Hello World!',
        }
    }
}
</script>

<style scoped>
h1 {
    /* 居中 */
    text-align: center;
}
</style>