<template>
    <div>
        <h1>人员列表</h1>
        <input type="text" placeholder="请输入姓名" v-model="name">
        <button @click="addPerson">添加</button>
        <h3 style="color: red;">Count Component 求和: {{ $store.state.sum }}</h3>
        <ul>
            <li v-for="p in personList" :key="p.id">
                name: {{ p.name }}
                <button class="btn-delete" @click="$store.commit('DELETE_PERSON', p.id)">删除</button>
            </li>
        </ul>
    </div>
</template>

<script>
import { nanoid } from 'nanoid'
export default {
    name: 'Person',
    data() {
        return {
            name: '',
        }
    },
    computed: {
        personList() {
            return this.$store.state.personList
        }
    },
    methods: {
        addPerson() {
            const personObj = {
                id: nanoid(),
                name: this.name
            }
            this.$store.commit('ADD_PERSON', personObj)
        }
    }
}
</script>

<style>
li button {
    display: none;
}

li:hover{
    background-color: #ddd;
}

li:hover button {
    display: inline-block;
    background-color: burlywood;
}
</style>