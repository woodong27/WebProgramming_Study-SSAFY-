<template>
  <div class="border">
    <h1>This is MyComponent</h1>
    <MyChild static-props="MyComponent(부모)에서 MyChild(자식)으로"
    :my-props="dynamicProps"
    @child-to-parent="parentGetEvent"
    @child-input='getDynamicData'
    />
  </div>
</template>

<script>
import MyChild from '@/components/MyChild'

export default {
  name: 'MyComponent',
  components: {
    MyChild,
  },
  data(){
    return {
      dynamicProps:"It's from MyComponent"
    }
  },
  methods:{
    parentGetEvent(inputData) {
      console.log('자식에서 발생한 이벤트')
      console.log(`자식에서 보낸 ${inputData}를 받음`)
    },
    getDynamicData(inputData) {
      console.log(`child에서 ${inputData}를 입력받음`)
    }
  }
}

</script>

<style>
  .border {
    border: solid;
  }
</style>
