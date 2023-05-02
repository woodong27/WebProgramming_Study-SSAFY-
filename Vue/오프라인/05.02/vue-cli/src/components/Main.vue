<template>
  <div class='main-border'>
    이건 Main
    <EachResult/>
  </div>
</template>

<script>
import EachResult from './EachResult.vue';
export default {
    name:'Main',
    components:{
        EachResult,
    }
}
</script>

<style>
.main-border{
  border:solid blue;
}
</style>