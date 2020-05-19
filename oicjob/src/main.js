import Vue from 'vue'
import App from './App.vue'
import router from './router'
import vuetify from './plugins/vuetify'
import axios from 'axios'
import { LoaderPlugin } from 'vue-google-login';
// import vuehead from './plugins/vuehead'

Vue.config.productionTip = false
axios.defaults.baseURL = "http://127.0.0.1:5000";
axios.defaults.headers.post["Content-Type"] =
  "application/json;charset=utf-8";
axios.defaults.headers.post["Access-Control-Allow-Origin"] =
  "http://127.0.0.1:5000";
Vue.prototype.$axios = axios

Vue.use(LoaderPlugin, {
  client_id: process.env.VUE_APP_CLIENT_ID
});

new Vue({
  router,
  vuetify,
  render: h => h(App)
}).$mount('#app')
