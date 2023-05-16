import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import router from '../router'

const API_URL = 'http://127.0.0.1:8000'

Vue.use(Vuex)


export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    articles: [],
    token: null
  },
  getters: {
    isLogin(state) {
      return state.token ? true:false
    }
  },
  mutations: {
    GET_ARTICLES(state, articles) {
      state.articles = articles
    },
    SAVE_TOKEN(state, token) {
      state.token=token
      // store에선 $router 불가 -> router를 import해와야 함
      router.push({name: 'ArticleView'})
    },
    DELETE_TOKEN(state) {
      state.token=null
      location.reload()
    }
  },
  actions: {
    async getArticles(context) {
      // axios({
      //   method: 'get',
      //   url: `${API_URL}/api/v1/articles/`,
      //   headers: {
      //     Authorization: `Token ${context.state.token}`
      //   }
      // })
      //   .then((res) => {
      //   // console.log(res, context)
      //     context.commit('GET_ARTICLES', res.data)
      //   })
      //   .catch((err) => {
      //   console.log(err)
      // })
      const result=await axios.get(`${API_URL}/api/v1/articles/`, {headers: {Authorization: `Token ${context.state.token}`}})
      context.commit('GET_ARTICLES', result.data)
    },
    async signUp(context, payload) {
      const username=payload.username
      const password1=payload.password1
      const password2=payload.password2

      // axios({
      //   method: 'post',
      //   url: `${API_URL}/accounts/signup/`,
      //   data: {username, password1, password2}
      // })
      // .then(response => {
      //   // 회원가입 하면 반환되는 토큰을 넘겨줌
      //   // 토큰은 어디에서든 쓸 수 있어야 함->state에 저장
      //   context.commit('SAVE_TOKEN',response.data.key)
      // })
      // .catch(error => {
      //   console.log(error)
      // })
      const result=await axios.post(`${API_URL}/accounts/signup/`, {username, password1, password2})
      context.commit('SAVE_TOKEN', result.data.key)
    },
    async logIn(context, payload) {
      const username=payload.username
      const password=payload.password

      // axios({
      //   method: 'post',
      //   url: `${API_URL}/accounts/login/`,
      //   data: {username, password}
      // })
      // .then(response => {
      //   context.commit('SAVE_TOKEN', response.data.key)
      // })
      // .catch(error => {
      //   console.log(error)
      // })
      const result=await axios.post(`${API_URL}/accounts/login/`, {username, password})
      context.commit('SAVE_TOKEN', result.data.key)
    },
    async logOut(context) {
      // axios({
      //   method: 'post',
      //   url: `${API_URL}/accounts/logout/`,
      //   headers: {
      //     Authorization: `Token ${context.state.token}`
      //   }
      // })
      // .then(() => {
      //   context.commit('DELETE_TOKEN')
      // })
      // .catch(err => {
      //   console.log(err)
      // })
      await axios.post(`${API_URL}/accounts/logout/`, {headers: {Authorization : `Token ${context.state.token}`}})
      context.commit('DELETE_TOKEN')
    }
  },
  modules: {
  }
})