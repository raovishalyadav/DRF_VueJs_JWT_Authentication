import { createRouter, createWebHistory } from 'vue-router'
import login from '../views/log-in.vue'
import signup from '../views/sign-up.vue'
import apidata from '../views/apidata.vue'


const routes = [
  {
    path: '/',
    name: 'log-in',
    component: login
  },
  {
    path: '/sign-up',
    name: 'signup',
    component: signup
  },
  {
    path: '/log-in',
    name: 'login',
    component: login
  },
  {
    path: '/apidata',
    name: 'apidata',
    component: apidata
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
