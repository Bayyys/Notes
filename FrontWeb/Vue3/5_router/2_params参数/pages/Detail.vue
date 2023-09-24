<template>
    <ul>
        <li>消息编号: {{ $route.params.id }}</li>
        <li>消息内容: {{ $route.params.title }}</li>
    </ul>
</template>

<script>
export default {
    name: 'Detail',
}
</script>

<style>
</style>