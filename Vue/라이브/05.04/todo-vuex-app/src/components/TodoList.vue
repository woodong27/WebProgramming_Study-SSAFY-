<template>
  <div>
    <h3>TodoList</h3>
    <TodoListItem v-for="(todo,index) in todos" :key="index" :todo-item="todo"/>
  </div>
</template>

<script>
import TodoListItem from './TodoListItem.vue'

export default {
    name: 'TodoList',
    components: {
        TodoListItem
    },
    computed: {
        todos() {
            return this.$store.state.todos
        }
    }
}
</script>

<style>

</style>