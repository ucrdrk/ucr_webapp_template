<template>
    <div class="faq">
      <NavBar navbartype='faq' />
      <div class="faqbox">
        
      </div>
    </div>
  </template>
  
  <style>
  .switch {
  margin-left: 15%;
  }
  .faq {
    height: 100vh;
    background-color: #1A1D1A;
  }
  .faqbox {
    height: auto;
    width: 500px;
    margin: auto;
    margin-top: 4em;
    background-color: white;
    border-radius: 10px;
    display: flex;
    flex-direction: column;
  }
  .faqtitle {
    text-align: center;
    margin: 51px auto 30px;
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
    margin-top: 10px;
    margin-bottom: 20px;
    border-radius: 30px;
  }
  </style>
  
  <script>
  import NavBar from '../components/NavBar.vue';

  import axios from 'axios'
  
  export default {
    name: "faq",
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
              .post('/api/account/faq', formData)
              .then(response => {
                this.$router.push('/login')
                console.log(response)
              })
              .error(error => {
                console.log(error)
              })
              
        }
    }
  };
  </script>
  