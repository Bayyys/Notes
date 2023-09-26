<template>
    <div class="son">
        <h1>Son Component</h1>
        <hr>
        <Dialog></Dialog>
    </div>
</template>

<script>
import Dialog from './Dialog.vue';
export default {
    name: 'Son',
    components: { Dialog },
}
</script>

<style scoped>
.son {
    background-color: orange;
    padding: 10px;
}
</style>