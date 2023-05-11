<template>
  <div class="article-list">
    <h3>Article List</h3>
    <!-- store에서 articles를 가져와서 하나씩 props를 써서 자식으로 보내줌 -->
    <ArticleListItem
    v-for="article in articles" :key="article.id"
    :article="article"
    />
  </div>
</template>

<script>
import ArticleListItem from './ArticleListItem.vue'

export default {
  name: 'ArticleList',
  components: {
    ArticleListItem
  },
  computed: {
    articles() {
      return this.$store.state.articles
    }
  }
}
</script>

<style>
.article-list {
  text-align: start;
}
</style>
