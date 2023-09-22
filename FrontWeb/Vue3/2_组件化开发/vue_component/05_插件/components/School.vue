<template>
    <div class="student">
        <h2>schoolName: {{ name }}</h2>
        <h2>address: {{ address }}</h2>
    </div>
</template>

<script>
export default {
    name: 'Student',
    data() {
        return {
            name: 'Middle School',
            address: 'Beijing'
        }
    },
}

</script>

<style>
.student {
    background-color: orange;
}
</style>