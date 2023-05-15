import Vue from 'vue'
import Router from 'vue-router'
// import HelloWorld from '@/components/HelloWorld'
// import index from '@/components/index'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      /* name: 'index', */
      component: () => import('@/components/container'),
      children:[
        {
          path: '/',
          name: 'q_first',
          component: () => import('@/components/q_first')
        },
        {
          path: 'q_second',
          name: 'q_second',
          component: () => import('@/components/q_second')
        },
        {
          path: 'q_third',
          name: 'q_third',
          component: () => import('@/components/q_third')
        }
      ]
    }
  ]
})
