<template>
    <div class="register">
      <NavBar navbartype='register' />
      <div class="registerbox">
        <form @submit.prevent="submitForm">
          <h3 class="registertitle">Register</h3>
          <p class="prompt">Username</p>
          <input type="text" class="userinput" v-model="username">
          <p class="prompt">Email</p>
          <input type="text" class="userinput" v-model="email">
          <p class="prompt">Password</p>
          <input type="password" class="userinput" v-model="password">
          <p class="prompt">Confirm Password</p>
          <input type="password" class="userinput" v-model="password2">
          <button>Submit</button>
        </form>
      </div>
    </div>
  </template>
  
  <style>
  .register {
    height: 100vh;
    background-color: #1A1D1A;
  }
  .registerbox {
    height: 670px;
    width: 500px;
    margin: auto;
    margin-top: 4em;
    background-color: white;
    border-radius: 10px;
    display: flex;
    flex-direction: column;
  }
  .registertitle {
    text-align: center;
    margin: 51px auto 55px;
    font-family: 'Inter', sans-serif;
    font-style: normal;
    font-weight: 700;
    font-size: 40px;
  }
  .prompt {
    margin-left: 15%;
    margin-bottom: 22px;
    font-family: 'Inter';
    font-style: normal;
    font-weight: 400;
    font-size: 20px;
  }
  .userinput {
    margin-left: 15%;
    margin-bottom: 22px;
    width: 330px;
    height: 45px;
    border-radius: 10px;
    font-size: large;
  }
  #submit {
    width: 330px;
    height: 55px;
    margin-left: 15%;
    margin-top: 30px;
    border-radius: 30px;
  }
  </style>
  
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
        email: "",
        password: "",
        password2: "",
      }
    },
    methods: {
        submitForm(){
          const formData = {
            username: this.username,
            email: this.email,
            password: this.password,
            password2: this.password2
          }
          axios
              .post('/api/account/register', formData)
              
        }
    }
  };
  </script>
  