<template>
  <div>
    <h3>FriedChicken</h3>
    <div>FriedChicken의 salt : {{ chickProps.salt }}</div>
    <ChickenChild
    :for-child="chickProps"
    @to-parent="fromChild"/>
  </div>
</template>

<script>
import ChickenChild from './ChickenChild.vue'

export default {
  name:'FriedChicken',
  components: {
    ChickenChild
  },
  props:{
    chickProps:Object
  },
  methods:{
    fromChild(datafromchild) {
      console.log(datafromchild)
      this.$emit('to-to-parent', datafromchild)
    }
  }
}
</script>

<style>

</style>