<template>
    <div class="child">
        <h1>Child Component</h1>
        <hr>
        <Son></Son>
    </div>
</template>

<script>
import Son from './Son.vue'
export default {
    name: 'Child',
    components: { Son },
}
</script>

<style scoped>
.child {
    background-color: skyblue;
    padding: 10px;
}
</style>