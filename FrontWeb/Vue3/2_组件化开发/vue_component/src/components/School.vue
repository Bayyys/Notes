<template>
    <div class="school">
        <h2>name: {{ name }}</h2>
        <h2>address: {{ address }}</h2>
    </div>
</template>

<script>
export default {
    name: 'School',
    data() {
        return {
            name: '小学',
            address: 'QD',
        }
    },
}

</script>

<style>
.school {
    background-color: aqua;
    font: italic bold 20px/30px Georgia, serif;
}
</style>