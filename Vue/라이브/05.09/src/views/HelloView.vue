<template>
  <div>
    <!-- HTML에서 바로 쓰기보단 data에서 정의해서 사용하는 것을 권장 -->
    <h1>Hello, {{ userName }}</h1>
  </div>
</template>

<script>
export default {
    name: 'HelloView',
    data() {
        return {
            userName: this.$route.params.userName
        }
    }
}
</script>

<style>

</style>