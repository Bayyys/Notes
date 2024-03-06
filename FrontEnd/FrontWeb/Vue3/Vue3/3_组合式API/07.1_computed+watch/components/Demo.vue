<template>
    <div>
        <h1>个人信息</h1>
        姓: <input type="text" v-model="person.firstName" />
        名: <input type="text" v-model="person.lastName" />
        年龄: <input type="number" v-model="person.age" />
        <hr>
        完整姓名(简写): {{ fullName }}
        <hr>
        完整姓名(合入属性): {{ person.fullName }}
        <hr>
        完整姓名(复杂写法): {{ fullName_complex }}

    </div>
</template>

<script>
import { ref, reactive, computed, watch } from 'vue'
export default {
    name: 'Demo',
    /* Vue2 写法, 此时能够得到setup内的数据 */
    // computed: {
    //     fullName() {
    //         return this.person.firstName + " " + this.person.lastName
    //     }
    // },
    setup(props, context) {
        const person = reactive({
            firstName: '张',
            lastName: '三',
            age: 18
        })

        // 1) computed ---- 简单写法
        const fullName = computed(() => {
            return person.firstName + " " + person.lastName
        })

        // 2) 直接给person添加属性
        person.fullName = computed(() => {
            return person.firstName + " " + person.lastName
        })

        // 3) computed ---- 复杂写法(也可以直接添加属性)
        const fullName_complex = computed({
            get() {
                return person.firstName + " " + person.lastName
            },
            set(val) {
                const names = val.split(' ')
                person.firstName = names[0]
                person.lastName = names[1]
            }
        })



        return { person, fullName, fullName_complex }
    }
}
</script>

<style></style>