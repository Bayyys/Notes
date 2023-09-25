export const funcMixin = {
    methods: {
        showName() {
            alert(this.name)
        }
    },
    data() {
        return {
            mixinParams: 'mixinParams'
        }
    }
}

export const funcMixin2 = {
    mounted() {
        console.log('mixin mounted')
    },
    data() {
        return {
            mixinParams2: 'mixinParams2'
        }
    },
}