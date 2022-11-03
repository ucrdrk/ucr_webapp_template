<template>
  <div class="site">
    <NavBar/>
    <div class="landing">
      <div class="right-side">
        <h2 class="statement">FPGA gaming. Simplified.</h2>
        <h3 class="sentence">Send ROM images to your MiSTer FPGA to play instantly.</h3>
        <router-link to="/login"><div>Get Started</div></router-link>
      </div>
      <div class="left-side">
        <img src="" alt="Top of image">
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
  
}
.statement{
  font-size: 64pt;
}
.sentence{
  font-size: 32pt;
}
</style>

<script>
// @ is an alias to /src
import NavBar from "../components/NavBar.vue";
//import Vue from "vue";

export default {
  name: "HomePage",
  components: {
    NavBar,
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
