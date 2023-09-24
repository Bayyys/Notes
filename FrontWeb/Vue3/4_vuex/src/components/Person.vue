<template>
    <div>
        <h1>人员列表</h1>
        <input ref="nameInput" type="text" placeholder="请输入姓名" v-model="name">
        <button @click="addPerson">添加</button>
        <button @click="showWords">展示一句话</button>
        <p v-show="words">{{ words }}</p>
        <h3 style="color: skyblue;">首位人员为: {{ first }}</h3>
        <h3 style="color: red;">Count Component 求和: {{ sum }}</h3>
        <ul>
            <li v-for="p in personList" :key="p.id">
                name: {{ p.name }}
                <button class="btn-delete" @click="$store.commit('myPerson/DELETE_PERSON', p.id)">删除</button>
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
            return this.$store.state.myPerson.personList
        },
        sum() {
            return this.$store.state.myCount.sum
        },
        first() {
            return this.$store.getters['myPerson/firstPersonName']
        },
        words() {
            return this.$store.state.myPerson.words
        }
    },
    methods: {
        addPerson() {
            const personObj = {
                id: nanoid(),
                name: this.name
            }
            this.$refs.nameInput.blur()
            this.name = ''
            this.$store.dispatch('myPerson/add_person', personObj)
        },
        showWords() {
            this.$store.dispatch('myPerson/show_words')
        }
    }
}
</script>

<style>
li button {
    display: none;
}

li:hover {
    background-color: #ddd;
}

li:hover button {
    display: inline-block;
    background-color: burlywood;
}
</style>