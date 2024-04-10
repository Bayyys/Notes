<template>
    <div>
        <h1>Banner Info: {{ msg }}</h1>
x
    </div>
</template>

<script>
export default {
    name: 'Banner',
    data() {
        return {
            msg: 'Hello World!',
        }
    },
    methods: {
        back() {
            this.$router.back();
        },
        forward() {
            this.$router.forward();
        },
        go() {
            this.$router.go(3);
        },
    },
}
</script>

<style scoped>
h1 {
    /* 居中 */
    text-align: center;
}
</style>