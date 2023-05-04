<template>
  <div>
    <div>
        <p>title : {{ $store.state.chicken.title }}</p>
        <p>salt : {{ $store.state.chicken.salt }}</p>
    </div>
    <button @click="btnClick" class='btn btn-primary'>소금이</button>
  </div>
</template>

<script>
export default {
    name:'ChickenChild',
    methods:{
        btnClick() {
            this.$store.dispatch('salting', 20)
        }
    }
}
</script>

<style>

</style>