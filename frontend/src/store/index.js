import Vue from "vue";
import Vuex from "vuex";
import axios from 'axios'
import VueAxios from 'vue-axios'

Vue.use(Vuex);
Vue.use(VueAxios, axios)

export default new Vuex.Store({
  state: {
    token: '',
    isAuthenticated: false
  },
  mutations: {
    initializeStore(state) {
      if( localStorage.getItem('token')) {
        state.token= localStorage.getItem('token')
        state.isAuthenticated = true
      }else {
        state.token = ''
        state.isAuthenticated = false
      }
    },
    setToken(state,token) {
      state.token = token
      state.isAuthenticated = true
    },
    removeToken(state) {
      state.token = ''
      state.isAuthenticated = false
    }
  },
  actions: {},
  modules: {},
});
