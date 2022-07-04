import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  {
    path: '/login',
    name: 'login',
    component: () => import('../views/Login.vue')
  },
  {
    path: '/register',
    name: 'register',
    component: () => import('../views/Register.vue')
  },
  {
    path: '/',
    name: 'home',
    component: () => import('../views/Episodes.vue')
  },
  {
    path: '/charts',
    name: 'charts',
    component: () => import('../views/Charts.vue')
  },
  {
    path: '/research',
    name: 'research',
    component: () => import('../views/Research.vue')
  }

]

const router = new VueRouter({
  routes
})

router.beforeResolve((to, _from, next) => {
  
  const token = localStorage.getItem('token')
  const sessionExpires = localStorage.getItem('sessionExpires')
  const now = new Date().getTime()

  if (
      to.path !== '/login' &&
      to.path !== '/register' &&
      (!token || sessionExpires <= now)
  ) next('/login')
  else next()
})


export default router
