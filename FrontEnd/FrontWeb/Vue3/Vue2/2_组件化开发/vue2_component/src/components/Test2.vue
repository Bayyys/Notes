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
    name: 'Test2',
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
    transition: 0.5s linear;
}

/* 进入的起点 */
.mymove-enter{
    transform: translateX(-100%);
}

/* 进入的终点 */
.mymove-enter-to{
    transform: translateX(0px);
}

.mymove-leave{
    transform: translateX(0px);
}

.mymove-leave-to{
    transform: translateX(-100%);
}

</style>