<template>
    <div>
        <ul :style="{opacity}">
            <li>news001 <input></li>
            <li>news002 <input></li>
            <li>news003 <input></li>
        </ul>
        <input type="checkbox" v-model="checked">勾选后可通过
    </div>
</template>

<script>
export default {
    name: 'News',
    data() {
        return {
            opacity: 1,
            checked: false,
        }
    },
    activated() {
        console.log('News组件被激活了')
        this.timer = setInterval(() => {
            console.log('@')
            this.opacity -= 0.01
            if (this.opacity <= 0) this.opacity = 1
        }, 16)
    },
    deactivated() {
        console.log('News组件失活了')
        clearInterval(this.timer)
    },
    // beforeRouteEnter: 通过路由规则进入组件之前调用
    beforeRouteEnter(to, from, next) {
        alert('若要退出请先勾选')
        console.log('beforeRouteEnter')
        next()
    },
    // beforeRouteLeave: 通过路由规则离开组件之前调用
    beforeRouteLeave(to, from, next) {
        console.log('beforeRouteLeave')
        if (!this.checked) {
            alert('请勾选后再离开')
            return
        }
        else { next() }
    },
}
</script>

<style></style>