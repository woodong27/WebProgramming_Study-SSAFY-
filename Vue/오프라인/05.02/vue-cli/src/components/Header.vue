<template>
  <div class='header-border'>
    이건 Header
    <Navigation/>
    <Search/>
  </div>
</template>

<script>
import Navigation from './Navigation.vue'
import Search from './Search.vue'
export default {
    name:'Header',
    components:{
      Navigation,
      Search
    }
}
</script>

<style>
.header-border{
  border:solid black;
}
</style>