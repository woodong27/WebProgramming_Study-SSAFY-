import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    todos: [
    ]
  },
  getters: {
    alltodosCount(state) {
      return state.todos.length
    },
    completedCount(state) {
      const completedTodos=state.todos.filter(todo=>todo.isCompleted)
      return completedTodos.length
    },
    notCompletedCount(state) {
      const notCompletedTodos=state.todos.filter(todo=>!(todo.isCompleted))
      return notCompletedTodos.length
    }
  },
  mutations: {
    CREATE_TODO(state, todoItem) {
      state.todos.push(todoItem)
    },
    DELETE_TODO(state, todoItem){
      // 해당 todoItem의 index를 찾아와서 삭제
      const index=state.todos.indexOf(todoItem)
      state.todos.splice(index,1)
    },
    UPDATE_TODO(state, todoItem) {
      // 모든 배열을 돌면서 수정
      // todos에서 클릭한 todoItem을 찾아서 해당 iscompleted를 반대로 뒤집어 줌
      state.todos=state.todos.map(todo => {
        if(todo===todoItem) {
          todo.isCompleted=!todo.isCompleted
        }
        return todo
      })
    },
    LOAD_TODOS(state) {
      const parsedTodos=JSON.parse(localStorage.getItem('todos'))
      state.todos=parsedTodos
    }
  },
  actions: {
    createTodo(context, todoTitle) {
      // console.log(context)
      const todoItem = {
        title: todoTitle,
        isCompleted: false
      }
      context.commit('CREATE_TODO', todoItem)
      context.dispatch('saveTodosToLocalStorage')
    },
    deleteTodo(context, todoItem) {
      context.commit("DELETE_TODO", todoItem)
    },
    updateTodo(context, todoItem) {
      context.commit('UPDATE_TODO', todoItem)
    },
    saveTodosToLocalStorage(context) {
      const jsonTodos=JSON.stringify(context.state.todos)
      localStorage.setItem('todos', jsonTodos)
    },
    loadTodos(context) {
      context.commit("LOAD_TODOS")
    }
  },
  modules: {
  }
})
