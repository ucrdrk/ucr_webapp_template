<template>
  <div class="login">
    <NavBar navbartype='login' />
    <div class="loginbox">
      <h3 class="logintitle">Login</h3>
      <p class="prompt">Email</p>
      <input type="text" name="user" class="userinput" id="">
      <p class="prompt">Password</p>
      <input type="password" name="pw" class="userinput" id="">
      <input type="button" value="Login" id="submit">
    </div>
  </div>
</template>

<style>
.login {
  height: 100vh;
  background-color: #1A1D1A;
}
.loginbox {
  height: 670px;
  width: 500px;
  margin: auto;
  margin-top: 4em;
  background-color: white;
  border-radius: 10px;
  display: flex;
  flex-direction: column;
}
.logintitle {
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

export default {
  name: "Login",
  components: {
    NavBar,
},
  data () {
    return {
      values: []
    }
  },
  created: function () {
    
  }
};
</script>
