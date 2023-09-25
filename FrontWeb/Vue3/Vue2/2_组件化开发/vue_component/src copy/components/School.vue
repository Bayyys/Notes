<template>
    <div class="myStyle">
        <h2>schoolName: {{ name }}</h2>
        <h2>address: {{ address }}</h2>
    </div>
</template>

<script>
export default {
    name: 'School',
    data() {
        return {
            name: 'Middle School',
            address: 'Beijing'
        }
    },
}

</script>

<style scoped>
.myStyle {
    background-color: orange;
}
</style>