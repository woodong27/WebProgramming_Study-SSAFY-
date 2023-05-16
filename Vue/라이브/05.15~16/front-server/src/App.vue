<template>
  <div id="app">
    <nav>
      <router-link :to="{ name: 'ArticleView' }">Articles</router-link> | 
      <router-link :to="{ name: 'SignUpView' }">SignUpPage</router-link> | 
      <router-link :to="{ name: 'LogInView' }">LogInPage</router-link>
    </nav>
    <button @click='logOut'>로그아웃</button>
    <router-view/>

  </div>
</template>

<script>
export default {
  name: 'App',
  methods: {
    logOut() {
      if (this.$store.getters.isLogin) {
        this.$store.dispatch('logOut')
      }
      else {
        alert('로그인이 필요합니다')
        this.$router.push({name: 'LogInView'})
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
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
