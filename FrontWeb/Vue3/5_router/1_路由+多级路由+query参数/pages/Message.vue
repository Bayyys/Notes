<template>
    <div>
        <ul>
            <li v-for="m in messageList" :key="m.id">
                <!-- 路由跳转并携带query参数, to的字符串写法 -->
                <router-link :to="`/myDetail?id=${m.id}&title=${m.title}`">{{ m.title }}</router-link>
                <!-- 路由跳转并携带query参数, to的对象写法 -->
                <router-link :to="{
                    path: 'myDetail',
                    query: {
                        id: m.id,
                        title: m.title
                    }
                }">{{ m.title }}</router-link>
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
    }

}
</script>

<style></style>