<template>
    <div class="child">
        <h1>Child Component</h1>
        <hr>
    </div>
</template>

<script>
import {ref} from 'vue'
export default {
    name: 'Child',
    setup() {
        let sum = ref(0)
        return new Promise((resolve, reject) => {
            setTimeout(() => {
                resolve({ sum })
            }, 500)
        })
    }
}
</script>

<style scoped>
.child {
    background-color: skyblue;
    padding: 10px;
}
</style>