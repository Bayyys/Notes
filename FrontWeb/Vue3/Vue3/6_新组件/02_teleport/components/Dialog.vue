<template>
    <div>
        <button @click="isShow = true">弹窗</button>
        <teleport to='body'>
            <div class="mask" v-show="isShow">
                <div class="dialog" v-show="isShow">
                    <h1>Dialog Component</h1>
                    <button @click="isShow = false">关闭</button>
                </div>
            </div>
        </teleport>
    </div>
</template>

<script>
import { ref, reactive } from 'vue';
export default {
    name: 'Dialog',
    setup() {
        const isShow = ref(false);
        return { isShow }
    },
}
</script>

<style>
.mask {
    position: absolute;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    background-color: rgba(0, 0, 0, .5);
}

.dialog {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    text-align: center;
    width: 300px;
    height: 300px;
    background-color: green;
}
</style>