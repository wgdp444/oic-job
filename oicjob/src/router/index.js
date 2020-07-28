import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Login from '../views/Login.vue'
import CreateAccount from '../views/CreateAccount.vue'
import VerboseScreen from '../views/VerboseScreen.vue'
import Edit from '../views/Edit.vue'
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
    component: CreateAccount,
    meta: {isBeforeCreateAccount: true}
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
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

// アクセス制限
router.beforeEach((to, from, next) => {
  console.log(1)
  Vue.GoogleAuth.then(auth2 => {
    // googleログインしていない場合 クソほど条件長くなったので要改善！！！！！！！！！！！！！！！！！！
    if (to.matched.some(record => (!record.meta.isPublic && !record.meta.isBeforeCreateAccount)) && (!auth2.isSignedIn.get() || !localStorage.getItem('access_token'))) {
      next({ path: '/login', query: { redirect: to.fullPath }});
    } else if (to.matched.some(record => record.meta.isBeforeCreateAccount) && localStorage.getItem('access_token') && auth2.isSignedIn.get()) {
      next({ path: '/', query: { redirect: to.fullPath }});
    } else {
      next();
    }
  });
});

export default router
