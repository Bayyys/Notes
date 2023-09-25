<template>
    <div class="student">
        <h2 @click="showName">name: {{ name }}</h2>
        <h2>sex: {{ sex }}</h2>
    </div>
</template>

<script>
// 引入混合对象
import { funcMixin } from '../mixin'

export default {
    name: 'Student',
    data() {
        return {
            name: '张三',
            sex: '男',
        }
    },
    mixins: [funcMixin],
}

</script>

<style>
.student {
    background-color: orange;
}
</style>