<template>
    <ul class="todo-main">
        <Item v-for="todoObj in todos" :key="todoObj.id" :todo="todoObj" :checkTodo="checkTodo" :deleteTodo="deleteTodo"></Item>
    </ul>
</template>

<script>
import Item from './Item.vue';
export default {
    name: 'List',
    components: { Item },
    props: ['todos', 'checkTodo', 'deleteTodo'],
}

</script>

<style scoped>
/*main*/
.todo-main {
    margin-left: 0px;
    border: 1px solid #ddd;
    border-radius: 2px;
    padding: 0px;
}

.todo-empty {
    height: 40px;
    line-height: 40px;
    border: 1px solid #ddd;
    border-radius: 2px;
    padding-left: 5px;
    margin-top: 10px;
}
</style>