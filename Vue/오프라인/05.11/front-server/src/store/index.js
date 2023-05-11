import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

const API_URL='http://127.0.0.1:8000'

Vue.use(Vuex)


export default new Vuex.Store({
  state: {
    articles: [
    ],
  },
  getters: {
  },
  mutations: {
    GET_ARTICLES(state, articles) {
      state.articles=articles
    }
  },
  actions: {
    async getArticles(context) {
      // 교안에서의 방법(기본)
      // axios({
      //   method: 'get',
      //   url: `${API_URL}/api/v1/articles/`
      // })
      // .then(response => {
      //   context.commit('GET_ARTICLES', response.data)
      // })
      // .catch(error => {
      //   console.log(error)
      // })

      //다른 방법
      // axios.get(`${API_URL}/api/v1/articles/`)
      // .then(response => console.log(response.data))
      // .catch(error => console.log(error))

      // 또 다른 방법(async/await)
      const result=await axios.get(`${API_URL}/api/v1/articles/`)
      context.commit('GET_ARTICLES', result.data)
    }
  },
  modules: {
  }
})
