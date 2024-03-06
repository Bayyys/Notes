<template>
    <div>
        <slot name="demo"></slot>
        <button @click="say">sayHello</button>
    </div>
</template>

<script>
export default {
    name: 'Demo',
    props: ['msg',],
    emits: ['sayHello'],
    setup(props, context) {
        console.log(props, context)
        console.log(context.emit)
        function say() {
            context.emit('sayHello', 'hello')
        }
        return { say }
    }
}
</script>

<style></style>