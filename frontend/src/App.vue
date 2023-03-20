<template>
  <div id="app">
    <router-view />
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'App',
  beforeCreate() {
    this.$store.commit('initializeStore')

    const token = this.$store.state.token

    if( token ) {
      axios.defaults.headers.common['Authorization'] = 'Token ' + token
    } else {
      axios.defaults.headers.common['Authorization'] = ''
    }
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Inria+Sans&family=Inter:wght@100;200;300;400;500;600;700;800;900&display=swap');
* {
  margin:0;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
</style>
