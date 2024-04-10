<template>
    <div>
        <h2>当前求和为: {{ sum }}</h2>
        <button @click="sum++">add</button>
        <h2>鼠标坐标: ({{ points.x }}, {{ points.y }})</h2>
    </div>
</template>

<script>
import { ref, reactive } from 'vue';
import showPoints from '../hooks/usePoint'
export default {
    name: 'Count',
    setup() {
        let sum = ref(0)
        const points = showPoints()
        return { sum, points }
    },
}
</script>

<style></style>