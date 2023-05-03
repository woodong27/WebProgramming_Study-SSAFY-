<template>
  <div id="app">
    <!-- props/emit 실습-->
    <h2 class="mini-title">[실습]</h2>
    <div>App의 salt : {{ chicken.salt }}</div>
    <FriedChicken
    :chick-props="chicken"
    @to-to-parent="fromChild"/>
    <hr>
    <h1>{{ count }}</h1>
  </div>
</template>

<script>
import FriedChicken from './components/FriedChicken.vue'
import axios from 'axios'

export default {
  name: 'App',
  components: {
    FriedChicken
  },
  data() {
    return {
      chicken: {
        salt:30,
        title:'치킨은 맛있다',
      },
      count:1,
      url:'https://koreanjson.com/todos'
    }
  },
  methods : {
    fromChild(fromFried) {
      console.log(fromFried)
      this.chicken.salt=fromFried
    },
  },
  beforeCreate() {
    console.log('beforeCreate')
  },
  async created() {
    console.log('created')
    const result=await axios.get(this.url)
    this.count=result.data[0].title
  },
  // 화면에 부착되기 전
  beforeMount () {
    console.log('beforeMount')
  },
  mounted() {
    console.log('mounted')
  },
  beforeUpdate() {
    console.log('beforeUpdated')
  },
  updated(){
    console.log('updated')
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
.mini-title {
  color: cornflowerblue;
}
</style>
