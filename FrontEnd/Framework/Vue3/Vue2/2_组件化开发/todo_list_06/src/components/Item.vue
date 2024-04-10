<template>
    <transition name="todo" appear>
        <li>
            <label>
                <input type="checkbox" :checked="todo.done" @change="handleCheck(todo.id)" />
                <span v-show="!todo.isEdit">{{ todo.title }}</span>
                <input type="text" ref="inputTitle" v-show="todo.isEdit" :value="todo.title"
                    @blur="handlerBlur(todo, $event)" />
            </label>
            <button class="btn btn-danger" @click="handleDelete(todo.id)">删除</button>
            <button v-show="!todo.isEdit" class="btn btn-edit" @click="handleEdit(todo)">编辑</button>
        </li>
    </transition>
</template>

<script>
export default {
    name: 'Item',
    // 声明接收todo对象 
    props: ['todo'],
    methods: {
        handleCheck(id) {
            this.$bus.$emit('checkTodo', id)
        },
        handleDelete(id) {
            if (window.confirm('确定删除吗？')) {
                this.$bus.$emit('deleteTodo', id)
            }
        },
        handleEdit(todo) {
            if (Object.prototype.hasOwnProperty.call(todo, 'isEdit')) {
                todo.isEdit = true
            }
            else {
                this.$set(todo, 'isEdit', true)
            }
            // 焦点定位到输入框
            this.$nextTick(() => {
                this.$refs.inputTitle.focus()
            })
        },
        handlerBlur(todo, e) {
            todo.isEdit = false
            if (!e.target.value.trim()) return alert('输入不能为空')
            this.$bus.$emit('updateTodo', todo.id, e.target.value)
        }
    }
}

</script>

<style scoped>
/* animate */
.todo-enter-active {
    animation: mymove 0.3s linear;
}

.todo-leave-active {
    animation: mymove 0.3s linear reverse;
}

@keyframes mymove {
    from {
        opacity: 0;
        transform: translateX(100px);
    }

    to {
        opacity: 1;
        transform: translateX(0);
    }
}

/*item*/
li {
    list-style: none;
    height: 36px;
    line-height: 36px;
    padding: 0 5px;
    border-bottom: 1px solid #ddd;
}

li label {
    float: left;
    cursor: pointer;
}

li label li input {
    vertical-align: middle;
    margin-right: 6px;
    position: relative;
    top: -1px;
}

li button {
    float: right;
    display: none;
    margin-top: 3px;
}

li:before {
    content: initial;
}

li:last-child {
    border-bottom: none;
}

li:hover {
    background-color: #ddd;
}

li:hover button {
    display: block;
}
</style>