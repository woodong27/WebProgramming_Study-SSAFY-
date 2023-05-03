<template>
  <div>
    <h5>ChildChicken</h5>
    <div>Childchicken의 salt : {{ forChild.salt }}</div>
    <button class="btn btn-primary" @click="salting">소금치기</button>
    <div v-if="salted">
        <div class="card">
            salt : {{ forChild.salt }}<br>
            title : {{ forChild.title }}
        </div>
    </div>
  </div>
</template>

<script>
export default {
    name:'ChickenChild',
    data() {
        return {
            salted:false,
        }
    },
    methods:{
        salting() {
            this.salted=!this.salted
            this.$emit('to-parent', 20)
        }
    },
    props:{
        forChild:Object
    }
}
</script>

<style>

</style>