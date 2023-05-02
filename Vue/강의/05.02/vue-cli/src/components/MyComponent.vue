<template>
  <div class="border">
    <h1>This is MyComponent</h1>
    <!-- 3. MyChild를 사용한다.-->
    <MyChild/>
  </div>
</template>

<!--Child Component를 MyComponent에 추가-->

<script>
// 1. Child Component를 import(가져온다)
import MyChild from '@/components/MyChild.vue'
export default {
    name: 'MyComponent',
    // 2. MyChild를 등록한다.
    components:{
        MyChild,
    }
}
</script>

<style>
.border{
  border:solid;
}
</style>