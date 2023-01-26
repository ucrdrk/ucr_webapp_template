import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import axios from "axios";
Vue.config.productionTip = false;

axios.deafults.baseURL = 'http://localhost:8000'

new Vue({
  router,
  store,
  axios,
  render: (h) => h(App),
}).$mount("#app");
