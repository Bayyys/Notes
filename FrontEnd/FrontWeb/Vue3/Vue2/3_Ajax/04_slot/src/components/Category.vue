<template>
    <div class="category">
        <h3>{{ title }}分类</h3>
        <slot :games="games"> 填充位置, 没有填充内容时显示这段文字 </slot>
    </div>
</template>

<script>
export default {
    name: 'Category',
    props: ['title'],
    data() {
        return {
            games: ['王者荣耀', '英雄联盟', '绝地求生', '穿越火线'],
        }
    },
}
</script>

<style scoped>
.category {
    border: 1px solid #ccc;
    font-size: 25px;
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