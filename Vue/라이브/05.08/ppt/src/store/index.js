import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate'
import myModule from './modules/myModules'

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersistedState()
  ],
  state: {
    message: 'message in state',
    age: 27
  },
  getters: {
    messageLength(state) {
      return state.message.length
    },
    // messageLength를 이용해서 새로운 값을 계산
    doubleLength(state, getters) {
      return getters.messageLength * 2
    },
  },
  mutations: {
    CHANGE_MESSAGE(state, message){
      // console.log(state)
      // console.log(message)
      state.message = message
    },
    // LOAD_MESSAGE(state) {
    //   const parsedMessage=JSON.parse(localStorage.getItem('message'))
    //   //parsing한 message가 있으면 그걸 출력, 없으면 빈 문자열 출력(삼항연산자)
    //   state.message=parsedMessage ? parsedMessage : ''
    // }
  },
  actions: {
    changeMessage(context, message){
      // console.log(context)
      // console.log(message)
      context.commit('CHANGE_MESSAGE', message)
      //바뀐 메시지를 localStorage에 저장
      context.dispatch('messageSaveToLocalStorage')
    },
    // //localStorage에 저장하는 메서드
    // messageSaveToLocalStorage(context) {
    //   const message=JSON.stringify(context.state.message)
    //   localStorage.setItem('message', message)
    // },
    // //localStorage에서 불러오는 메서드
    // loadMessage(context) {
    //   context.commit('LOAD_MESSAGE')
    // }
  },
  modules: {
    myModule
  }
})
