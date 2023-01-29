<template>
    <div class="site">
        <NavBar navbartype="login"/>
        <div class="content">
            <div class="mystuff">
                <div class="fpga">
                    <h2>FPGA board connected</h2>
                </div>
                <div class="mygames">

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
    height: 100vh;
    background-color: #ffffff;
}
.mystuff {

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