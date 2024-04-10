<template>
    <div>
        <button @click="isShow = !isShow">Toggle</button>
        <transition appear
            name="animate__animated animate__bounce"
            enter-active-class="animate__backInLeft"
            leave-active-class="animate__backOutUp">
            <h1 v-show="isShow" class="come">{{ name }}</h1>
        </transition>
    </div>
</template>

<script>
import 'animate.css'
export default {
    name: 'Test3',
    data() {
        return {
            name: 'Test Component',
            isShow: true
        }
    },
}
</script>

<style scoped>
h1 {
    background-color: skyblue;
}
</style>