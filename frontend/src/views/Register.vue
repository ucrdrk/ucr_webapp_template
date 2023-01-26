
<template>
  <div class = "register">
    <h1>Register</h1>
    <form @submit.prevent="submitForm">
      <input type="email" name = "username" v-model = "username">
      <input type = "password" name = "password" v-model = "password">
      <button type = "submit">Sign up</button>
    </form>
  </div>
</template>
  

  
  <script>
  import NavBar from '../components/NavBar.vue';

  import axios from 'axios'
  
  export default {
    name: "Register",
    components: {
      NavBar,
    },
    data () {
      return {
        username: "",
        password: "",
      }
    },
    methods: {
        submitForm(e){
          const formData = {
            username: this.username,
            email: this.email,
            password: this.password,
          }
          axios
              .post('/api/account/register', formData)
              .then(response => {
                this.$router.push('/login')
                console.log(response)
              })
              .catch(error=> {
                console.log(error)
              })
        }
    }
  };
  </script>
  