<template>
    <div id="root">
        <div class="todo-container">
            <div class="todo-wrap">
                <UserHeader @addTodo="addTodo"></UserHeader>
                <List :todos="todos"></List>
                <UserFooter :todos="todos" @allTodo="allTodo" @clearTodo="clearTodo"></UserFooter>
            </div>
        </div>
    </div>
</template>

<script>
import UserHeader from './components/UserHeader.vue'
import UserFooter from './components/UserFooter.vue'
import List from './components/List.vue'

export default {
    name: 'App',
    components: { UserHeader, UserFooter, List },
    data() {
        return {
            todos: JSON.parse(localStorage.getItem('todos')) || []
        }
    },
    methods: {
        addTodo(todoObj) {
            this.todos.unshift(todoObj)
        },
        checkTodo(id) {
            this.todos.forEach((todo) => {
                if (todo.id === id) todo.done = !todo.done
            })
        },
        deleteTodo(id) {
            this.todos = this.todos.filter((todo) => {
                return todo.id !== id
            })
        },
        updateTodo(id, title) {
            this.todos.forEach((todo) => {
                if (todo.id === id) todo.title = title
            })
        },
        allTodo(done) {
            this.todos.forEach((todo) => {
                todo.done = done
            })
        },
        clearTodo() {
            this.todos = this.todos.filter((todo) => {
                return !todo.done
            })
        }
    },
    watch: {
        todos: {
            deep: true,
            handler() {
                localStorage.setItem('todos', JSON.stringify(this.todos))
            }
        }
    },
    mounted() {
        this.$bus.$on('addTodo', (todoObj) => {
            this.addTodo.call(this, todoObj)
        })
        this.$bus.$on('checkTodo', (id) => {
            this.checkTodo.call(this, id)
        })
        this.$bus.$on('deleteTodo', (id) => {
            this.deleteTodo.call(this, id)
        })
        this.$bus.$on('updateTodo', (id, title) => {
            this.updateTodo.call(this, id, title)
        })
    },
    beforeDestroy() {
        this.$bus.$off('addTodo')
        this.$bus.$off('checkTodo')
        this.$bus.$off('deleteTodo')
        this.$bus.$off('updateTodo')
    }
}
</script>

<style>
/*base*/
body {
    background: #fff;
}

.btn {
    display: inline-block;
    padding: 4px 12px;
    margin-bottom: 0;
    font-size: 14px;
    line-height: 20px;
    text-align: center;
    vertical-align: middle;
    cursor: pointer;
    box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.2), 0 1px 2px rgba(0, 0, 0, 0.05);
    border-radius: 4px;
}

.btn-danger {
    color: #fff;
    background-color: #da4f49;
    border: 1px solid #bd362f;
}

.btn-edit {
    color: #fff;
    background-color: rgb(47, 171, 94);
    border: 1px solid rgb(96, 156, 7);
    margin-right: 2px;
}

.btn-danger:hover {
    color: #fff;
    background-color: #bd362f;
}

.btn:focus {
    outline: none;
}

.todo-container {
    width: 600px;
    margin: 0 auto;
}

.todo-container .todo-wrap {
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 5px;
}
</style>