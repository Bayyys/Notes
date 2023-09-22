<template>
    <div class="school">
        <h2>学校姓名: {{ name }}</h2>
        <h2>学校地址: {{ address }}</h2>
        <button @click="giveSchoolName">传递学校名</button>
    </div>
</template>

<script>
export default {
    name: 'School',
    props: ["getSchoolName"],
    data() {
        return {
            name: 'Middle School',
            address: 'Beijing'
        }
    },
    methods: {
        giveSchoolName() {
            this.getSchoolName(this.name)
        }
    }
}

</script>

<style scoped>
.school {
    background-color: orange;
    padding: 5px;
    margin-top: 5px;
}
</style>