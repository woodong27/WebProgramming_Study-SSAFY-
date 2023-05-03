<template>
  <div>
    <h3>This is child component</h3>
    <p>{{ staticProps }}</p>
    <p>{{ myProps }}</p>
    <button @click="childToParent">클릭</button>
    <input type="text" v-model='childInputData' @keyup.enter='childInput'>
  </div>
</template>

<script>
export default {
  name: 'MyChild',
  props:{
    staticProps:String,
    myProps:String,
  },
  methods:{
    childToParent() {
      this.$emit('child-to-parent', 'child data')
    },
    childInput() {
      this.$emit('child-input', this.childInputData)
      this.childInputData=""
    }
  },
  data() {
    return {
      childInputData:null,
    }
  }
}
</script>

<style>
  
</style>
