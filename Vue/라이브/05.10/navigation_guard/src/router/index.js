import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import HelloView from '@/views/HelloView.vue'
import LoginView from '@/views/LoginView.vue'
import NotFound404View from '../views/NotFound404View.vue'
import DogView from '../views/DogView.vue'

Vue.use(VueRouter)

const isLoggedIn=true

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/hello/:userName',
    name: 'hello',
    component: HelloView
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView,
    // Router Guard
    beforeEnter(to, from, next) {
      if (isLoggedIn) {
        console.log('로그인 되어있음')
        next({name:'home'})
      }
      else {
        next()
      }
    }
  },
  {
    path: '/404',
    name: 'NotFound404',
    component: NotFound404View
  },
  {
    path: '/dog/:breed',
    name: 'dog',
    component: DogView
  },
  // 모든 경로에 대해서 404 page로 redirect 시키기
  // routes 최하단부에 작성해야 함
  {
    path: '*',
    redirect: '/404'
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

// router/index.js
// global navigation guard
// router.beforeEach((to, from, next) => {
//   // CODE HERE
//   // 로그인 여부를 판단하고 로그인이 필요한 페이지를 지정
//   const isLoggedIn=false
//   const allowAuthPages=['login']
//   // const authPages=['hello']
//   const isAuthRequired=!allowAuthPages.includes(to.name)
  
//   // 로그인이 되어있지 않고, 로그인이 필요한 페이지면 로그인 페이지로 이동
//   if (isAuthRequired && !isLoggedIn) {
//     console.log('Login으로 이동')
//     next({name:'login'})
//   }
//   else {
//     console.log('to로 이동')
//     next()
//   }
// })
export default router
