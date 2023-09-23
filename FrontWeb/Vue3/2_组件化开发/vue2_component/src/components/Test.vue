<template>
    <div>
        <button @click="isShow = !isShow">Toggle</button>
        <transition name="mymove" appear>
            <h1 v-show="isShow" class="come">{{ name }}</h1>
        </transition>
    </div>
</template>

<script>
export default {
    name: 'Test',
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

.mymove-enter-active{
    animation: myFrames 1s;
}

.mymove-leave-active{
    animation: myFrames 1s reverse;
}

@keyframes myFrames {
    from {
        transform: translateX(-100%);
    }
    to {
        transform: translateX(0px);
    }
}
</style>