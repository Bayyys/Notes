<template>
    <div class="student">
        <h2 @click="showName">SchoolName: {{ name }}</h2>
        <h2>address: {{ address }}</h2>
    </div>
</template>

<script>
// 引入混合对象
import { funcMixin } from '../mixin'

export default {
    name: 'Student',
    data() {
        return {
            name: 'Middle School',
            address: 'Beijing'
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