<template>
    <div class="site">
        <NavBar navbartype="login"/>
        <div class="content">
            <div class="mystuff">
                <div class="fpga">
                    <h2 class="fpgatitle">FPGA board connected</h2>
                    <div class="sendbutton">Send games to board</div>
                </div>
                <div class="mygames">
                    <h2>My Games</h2>
                </div>
            </div>
            <div class="catalog">

            </div>
        </div>
    </div>
</template>

<style>
.site {
    display: flex;
    flex-direction: column;
    height: 100vh;
    background-color: #1A1D1A;
}
.content {
    display: flex;
    flex-direction: column;
    height: 100vh;
    background-color: #ffffff;

}
.mystuff {
    display: flex;
    flex-direction: row;
    height: 400px;
    /*background-color: red;*/
    margin: 30px;
}
.fpga {
    display: flex;
    flex-direction: column;
    width: 40%;
}
.fpgatitle {
    width: 40%;
}
.sendbutton {
    text-align: center;
    vertical-align: middle;
    height: 90px;
    line-height: 90px;
    width: 288px;
    background-color: #6D8B9C;
    border-radius: 15px;
    font-size: 24px;
    margin-top: 20%;
}
.mygames {
    display: flex;
}
</style>

<script>
    import NavBar from "../components/NavBar.vue";

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