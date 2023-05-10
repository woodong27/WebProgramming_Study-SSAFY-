<template>
  <div class="about">
    <h1>This is an about page</h1>

    <!-- 선언적 방식 네비게이션 -->
    <router-link :to="{name:'home'}">Home</router-link><br>

    <!-- 프로그래밍 방식 네비게이션 -->
    <button @click='toHome'>Home으로 이동</button><br>
    <hr>
    <input type="text" @keyup.enter="goToHello" v-model="inputData">
  </div>
</template>

<script>
export default {
  name: 'AboutView',
  data() {
    return {
      inputData: null
    }
  },
  methods: {
    toHome() {
      this.$router.push({name:'home'})
    },
    goToHello() {
      this.$router.push({name:'hello', params:{userName:this.inputData}})
      this.inputData=null
    }
  }
}
</script>
