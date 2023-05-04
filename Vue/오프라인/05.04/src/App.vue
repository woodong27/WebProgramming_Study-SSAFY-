<template>
  <div id="app">
    {{ msg }}
    <!-- <HelloWorld/> -->
    <hr>
    <h2>Actions / Mutations</h2>
    <FriedChicken/>
    <hr>
    <h2>Getters</h2>
    <div>"{{ msg }}"의 길이 : {{ msgLen }}</div>
    <hr>
    <h2>v-for</h2>
    <div>{{ str }}</div>
    <span v-for="(word,idx) in str" :key='idx'>
      {{word}}
    </span>
    <div>{{ arr }}</div>
    <div v-for="(obj, index) in arr" :key='index'>
      name{{ obj.id }} : {{ obj.name }}
    </div>
    <hr>
    <h2>v-on</h2>
    <div>{{ num }}</div>
    <button @click="increasing" class='btn btn-primary'>1씩 커짐</button>
  </div>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
import FriedChicken from './components/FriedChicken.vue'

export default {
  name: 'App',
  components: {
    // HelloWorld
    FriedChicken
  },
  data() {
    return {
      msg: this.$store.state.msg,
      str: 'Hello, App!',
      arr: [
        {id:1, name:'woo'},
        {id:2, name:'sun'}
      ],
      num: 0
    }
  },
  methods: {
    increasing() {
      console.log(this.num+1)
      this.num=this.num+1
    }
  },
  computed: {
    msgLen() {
      return this.$store.getters.msgLength
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
h2 {
  color: cornflowerblue;
}
</style>
