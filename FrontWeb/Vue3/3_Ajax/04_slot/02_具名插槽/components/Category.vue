<template>
    <div class="category">
        <h3>{{ title }}分类</h3>
        <slot name="center">
            中部填充位置, 没有填充内容时显示这段文字
        </slot>
        <slot name="footer">
            底部填充位置
        </slot>
    </div>
</template>

<script>
export default {
    name: 'Category',
    props: ['title', 'listData'],
    data() {
        return {
        }
    },
}
</script>

<style scoped>
.category {
    border: 1px solid #ccc;
    font-size: 15px;
    background-color: skyblue;
    width: 200px;
    height: 350px;
    padding: 10px;
    margin: 10px;
}

h3 {
    text-align: center;
    font: bold;
    background-color: cornflowerblue;
}

img {
    width: 100%;
}

video {
    width: 100%;
}
</style>