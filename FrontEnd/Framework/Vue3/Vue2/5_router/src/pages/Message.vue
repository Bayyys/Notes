<template>
    <div>
        <ul>
            <li v-for="m in messageList" :key="m.id">
                <!-- 路由跳转并携带params参数, to的字符串写法 -->
                <router-link :to="`/home/message/detail/${m.id}/${m.title}`">{{ m.title }}</router-link>
                <router-link :to="{
                    name: 'myDetail',
                    params: {
                        id: m.id,
                        title: m.title
                    }
                }">{{ m.title }}</router-link>
                <button @click="pushShow(m)">push查看</button>
                <button @click="replaceShow(m)">replace查看</button>
            </li>
        </ul>
        <hr>
        <router-view></router-view>
    </div>
</template>

<script>
export default {
    name: 'Message',
    data() {
        return {
            messageList: [
                { id: 1, title: 'message001' },
                { id: 2, title: 'message002' },
                { id: 3, title: 'message003' },
            ]
        }
    },
    methods: {
        pushShow(m) {
            this.$router.push({
                name: 'myDetail',
                params: {
                    id: m.id,
                    title: m.title
                }
            })
        },
        replaceShow(m) {
            this.$router.replace({
                name: 'myDetail',
                params: {
                    id: m.id,
                    title: m.title
                }
            })
        },
    },
}
</script>

<style></style>