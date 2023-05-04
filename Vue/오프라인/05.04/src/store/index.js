import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    msg: 'Hello Vue!',
    chicken: {
      title:'치킨',
      salt:30
    }
  },
  getters: {
    msgLength(state) {
      return state.msg.length
    }
  },
  mutations: {
    CHANGE(state, newMsg) {
      console.log(state, newMsg)
      state.msg=newMsg
    },
    SALTING(state, newSalt){
      state.chicken.salt=newSalt
    }
  },
  actions: {
    changeMsg(context, newMsg) {
      console.log(context, newMsg)
      context.commit('CHANGE', newMsg)
    },
    salting(context, newSalt) {
      context.commit('SALTING', newSalt)
    }
  },
  modules: {

  }
})
