<template>
  <div id="app">
    <Header/>
    <Main/>
    <hr>
    <!--text interpoation/v-html 실습-->
    <h4 class='mini-title'>Text interpolation / v-html </h4>
    <p>message : {{ message }}</p>
    <p>{{ rawHTML }}</p>
    <!--v-html은 웬만하면 사용하지 않는 것을 권장, 그냥 쓰지 마-->
    <p v-html='rawHTML'></p>
    <hr>

    <!--v-show-->
    <h4 class="mini-title">v-show</h4>
    <p v-show='isActive'>isActive가 {{ isActive }}일때만 보임</p>
    <hr>

    <!-- v-if/v-else-if/v-else 실습 -->
    <h4 class='mini-title'>v-if / v-else-if / v-else</h4>
    <div v-if='seen1'>
      <div>a</div>
      <div>b</div>
      <div>c</div>
    </div>
    <div v-else-if='seen2'>
      <div>d</div>
      <div>e</div>
      <div>f</div>
    </div>
    <div v-else>
      <div>g</div>
      <div>h</div>
      <div>i</div>
    </div>
    <button @click='clickbtn'>go</button>
    <hr>

    <!-- v-for 실습 -->
    <h4 class='mini-title'>v-for</h4>
    <div v-for="bucket in buckets" :key='bucket.id'>
      <div v-if='bucket.done'>{{bucket.id}}번째 일 : {{bucket.text}}</div>
    </div>
  </div>
</template>

<script>
import Header from './components/Header.vue';
import Main from './components/Main.vue';

export default{
  name: 'App',
  components: {
    Header,
    Main
  },
  data(){
    return {
      message:'hi',
      rawHTML:"<span style='color:red'>hello</span>",
      isActive:true,
      seen1:true,
      seen2:false,
      buckets:[
        {id:1, text:'일1', done:true},
        {id:2, text:'일2', done:true},
        {id:3, text:'일3', done:false},
        {id:4, text:'일4', done:true},
        {id:5, text:'일5', done:false},
      ]
    }
  },
  methods:{
    clickbtn() {
      if (this.seen1===true){
        this.seen2=true
        this.seen1=false
      }
      else if(this.seen2===true){
        this.seen2=false
      }
      else {
        this.seen1=true
      }
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
.mini-title{
  color:cornflowerblue;
}
</style>
