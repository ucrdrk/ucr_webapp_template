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
                    <div class="myList">
                      <div v-for="game in games" :key="game.id" class="card">
                        <GameComp :info="game"/>
                      </div>
                    </div>
                </div>
            </div>
            <div class="catalog">
              <h2>Catalog</h2>
              <div class="theList">
                <div v-for="game in allGames" :key="game.id" class="card">
                  <GameComp :info="game"/>
                </div>
              </div>
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
.myList{
  display: grid;
  grid-template-columns: 5fr 5fr 5fr 5fr;
  grid-template-rows: 5fr 5fr 5fr 5fr;
  column-gap: 1rem;
  row-gap: 250px;
  margin: 0 auto;
}
.theList{
  display: grid;
  grid-template-columns: 5fr 5fr 5fr 5fr 5fr;
  grid-template-rows: 5fr 5fr 5fr 5fr;
  column-gap: 1rem;
  row-gap: 100px;
  margin: 0 auto;
}
.card {
  width: 186px;
  border-radius: .5rem;
  padding: 1rem;
  margin-bottom: 1rem;
}
.catalog {
  width: 75%;
  margin: auto;
}
</style>

<script>
  import myGames from "../assets/userGames.json"
  import allGames from "../assets/catalogGames.json"
  import GameComp from "../components/GameComp.vue";
  import NavBar from "../components/NavBar.vue";

  export default {
    name: "HomePage",
    components: {
      NavBar,
      GameComp
        },
    data () {
      return {
        games: myGames,
        allGames: allGames
      }
    },
    methods: {
      getAllGames(){
        this.$http.get('/api/games/all-games').then((response) =>{
          this.allGames = response.data.results
        })
        .catch((err) =>{
          console.log(err)
        })
      }
    },
    created(){
      this.getAllGames()
    }
};
</script>