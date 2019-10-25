import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import index from '@/components/index'
import login from '../components/login'
import list from '../components/list'
import edit from '../components/edit'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
    	path:'/index',
    	name:'index',
    	component:index
    },
    {
    	path:'/login',
    	name:login,
    	component:login
    },
    {
    	path:'/list',
    	name:list,
    	component:list
    },
    {
    	path:'/edit',
    	name:edit,
    	component:edit
    }, 
  ],
mode:'history',
})
