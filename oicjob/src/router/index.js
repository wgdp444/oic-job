import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Login from '../views/Login.vue'
import CreateAccount from '../views/CreateAccount.vue'
import VerboseScreen from '../views/VerboseScreen.vue'
import Edit from '../views/Edit.vue'
import Register from '../views/Register.vue'
// import HeaderItem from '../components/HeaderItem.vue'

Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
    meta: {isPublic: true},
  },
  {
    path: '/create_account',
    name: 'CreateAccount',
    component: CreateAccount
  },
  {
    path: '/verbose_screen',
    name: 'VerboseScreen',
    component: VerboseScreen
  },
  {
    path: '/edit',
    name: 'Edit',
    component: Edit
  },
  {
    path: '/register',
    name: 'Register',
    component: Register
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {
  console.log(1)
  Vue.GoogleAuth.then(auth2 => {
    if (to.matched.some(record => !record.meta.isPublic) && !auth2.isSignedIn.get()) {
      next({ path: '/login', query: { redirect: to.fullPath }});
    } else {
      next();
    }
  });
});

export default router
