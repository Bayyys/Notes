<template>
    <section class="jumbotron">
        <h3 class="jumbotron-heading">Search Github Users</h3>
        <div>
            <input ref="keyType" type="text" placeholder="enter the name you search" v-model="keyWord"
                @keyup.enter="enterSearchUsers" @blur="searchUsers" />&nbsp;
            <button @click="searchUsers">Search</button>
        </div>
    </section>
</template>

<script>
import axios from 'axios'
export default {
    name: 'Search',
    data() {
        return {
            keyWord: '',
        }
    },
    methods: {
        searchUsers() {
            this.$bus.$emit('updateListData', { isFirst: false, isLoading: true, errMsg: '', users: [] })
            axios.get(`https://api.github.com/search/users?q=${this.keyWord}`).then(
                response => {
                    this.$bus.$emit('updateListData', { isLoading: false, errMsg: '', users: response.data.items })
                },
                error => {
                    this.$bus.$emit('updateListData', { isLoading: false, errMsg: error.message, users: [] })
                }
            )
        },
        enterSearchUsers() {
            this.$refs.keyType.blur()
        }
    },
}
</script>

<style scoped></style>