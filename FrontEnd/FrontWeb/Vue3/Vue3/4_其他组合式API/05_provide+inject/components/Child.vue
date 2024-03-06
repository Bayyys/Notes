<template>
    <div class="child">
        <h1>{{ msg }}</h1>
        <hr>
        <Son></Son>
    </div>
</template>

<script>
import { ref } from 'vue'
import Son from './Son.vue'
export default {
    name: 'Child',
    components: { Son },
    setup() {
        const msg = ref("Child Component")
        return { msg }
    }
}
</script>

<style scoped>
.child {
    background-color: skyblue;
    padding: 10px;
}
</style>