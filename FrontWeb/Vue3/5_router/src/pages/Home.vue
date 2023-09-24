<template>
    <div>
        <h2>Home组件内容</h2>
        <div>
            <ul class="nav nav-tabs">
                <li>
                    <router-link class="list-group-item" active-class="active" :to="{name: 'myNews'}">News</router-link>
                </li>
                <li>
                     <router-link class="list-group-item" active-class="active" :to="{name: 'myMessage'}">Message</router-link>
                </li>
            </ul>
            <div>
                <keep-alive include="News">
                    <router-view></router-view>
                </keep-alive>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Home',
}
</script>

<style></style>