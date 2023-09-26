<template>
    <div class="son">
        <h1>{{ msg }}, {{ car.name }} --- {{ car.price }}</h1>
        <hr>
    </div>
</template>

<script>
import { ref, inject } from 'vue'
export default {
    name: 'Son',
    setup() {
        const msg = ref("Son Component")
        const car = inject('car')
        return { msg, car }
    }
}
</script>

<style scoped>
.son {
    background-color: orange;
    padding: 10px;
}
</style>