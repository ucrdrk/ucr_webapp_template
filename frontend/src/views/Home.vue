<template>
  <div class="site">
    <GameComp gamebartype='home'/>
    <NavBar navbartype='home' />
    <div class="landing">
      <div class="right-side">
        <h2 class="statement">FPGA gaming. Simplified.</h2>
        <h3 class="sentence">Send ROM images to your MiSTer FPGA to play instantly.</h3>
        <router-link to="/login"><div class="landing-button">Get started</div></router-link>
      </div>
      <div class="left-side">
        <img src="../assets/cloud_games.png" alt="Top of image" width="520px">
      </div>
    </div>
  </div>
</template>

<style>
@import url('https://fonts.googleapis.com/css2?family=Inria+Sans&family=Inter:wght@100;200;300;400;500;600;700;800;900&display=swap');
.site {
  display: flex;
  flex-direction: column;
  height: 100vh;
  background-color: #1A1D1A;
}
.landing {
  display: flex;
  flex: 1 1 auto;
  margin: auto 10%;
}
.right-side{
  font-family: 'Inter', sans-serif;
  display: flex;
  flex-direction: column;
  margin-top: 10%;
  width: 50%;
  color: #8AB0AB;
}
.left-side{
margin-left: 10%;
}
.statement{
  font-size: 64px;
  max-width: 495px;
}
.sentence{
  margin-top: 40px;
  font-size: 32px;
  max-width: 452px;
}
.landing-button {
  height: 86px;
  line-height: 86px;
  width: 224px;
  margin-top: 88px;
  margin-left: 87px;
  background-color: #6D8B9C;
  color: #1A1D1A;
  font-size: 32px;
  font-weight: 700;
  border-radius: 10px;
  vertical-align: middle;
  text-align: center;
}
</style>

<script>
// @ is an alias to /src
import NavBar from "../components/NavBar.vue";
import GameComp from "../components/GameComp.vue";
//import Vue from "vue";

export default {
  name: "HomePage",
  components: {
    NavBar,
    GameComp,
},
  data () {
    return {
      values: []
    }
  },
  created: function () {
    this.$http.get('/api/foos/').then((response) => {
      console.log(response.data)
      this.values = response.data
    })
    console.log("Created")
  }
};
</script>
