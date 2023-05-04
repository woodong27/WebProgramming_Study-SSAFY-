import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    todos:[
    ]
  },
  getters: {
  },
  mutations: {
    CREATE_TODO(state, newTodo) {
      state.todos.push(newTodo)
    }
  },
  actions: {
    createTodo(context, todoTitle) {
      console.log(context)
      const newTodo={
        title: todoTitle,
        isCompleted: false
      }
      context.commit('CREATE_TODO', newTodo)
    }
  },
  modules: {
  }
})
