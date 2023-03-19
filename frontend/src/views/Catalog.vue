<template>
    <div class="site">
      <FAQBar faqbartype="home"/>
        <div class="content">
            <div class="mystuff">
                <div class="fpga">
                    <h2 class="fpgatitle">FPGA board connected</h2>
                    <div class="fpgainfo">
                      <h3 class="storageused">Storage Used:</h3>
                      <h3 class="storageleft">Storage Remaining:</h3>
                      <h3 class="totalstorage">Total Storage</h3>
                    </div>
                    <div class="sendbutton">Send games to board</div>
                    <div class="filter">
                      <label class="title" for="menu">Select a filter:</label>
                      <div class="filterops">
                       <select id="menu" name="menu">
                         <option value="option4">None</option>
                         <option value="option1">Category</option>
                         <option value="option2">Manufacturer</option>
                         <option value="option3">Game Type</option>
                       </select>
                      </div>
                   </div>
              </div>
             
              <div class="mygames">
                    <h2 class="myGamestitle">My Games</h2>
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
.filter{
  display: flex;
  flex-direction: row;
  background-color: #6D8B9C;
  color: white;
  height: 30px;
  width: 288px;
  justify-content: bottom;
  margin-top:5%;
  margin-bottom: 10%;
  border-radius: 10px;
}
.title{
  display: flex;
  justify-content: top;
  margin-top: 0px;
  font-size: medium;
  font-style: bold;
  width: 100px;
  color: black;
  padding-right: 20px;
  padding-bottom: 20px;
}
.filterops {
  font-size: 16px;
  border: none;
  cursor: pointer;
  height: 30px;
  padding-right:20px;
  justify-content: bottom;
}

/* Dropdown button on hover & focus */
/* .dropbtn:hover, .dropbtn:focus {
} */

/* The container <div> - needed to position the dropdown content */
.dropdown {
  position: relative;
  display: inline-block;
}

/* Dropdown Content (Hidden by Default) */
.dropdown-content {
  display: none;
  position: absolute;
  background-color: #f1f1f1;
  min-width: 160px;
  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
  z-index: 1;
}

.content {
    display: flex;
    flex-direction: column;
    height: 100vh;
    background-color: #ffffff;
    padding-bottom: 30px;

}
.myGamestitle{
  padding-left:20px;
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
    padding:20px;
}
.sendbutton {
    text-align: center;
    vertical-align: middle;
    height: 60px;
    line-height: 90px;
    width: 288px;
    background-color: #6D8B9C;
    border-radius: 15px;
    font-size: 24px;
    margin-top: 10%;
    padding-bottom: 10%;
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
    import FAQBar from "../components/FAQBar.vue";
    var myFunction = function() {
      document.getElementById("myDropdown").classList.toggle("show");
    }
    export default {
        name: "HomePage",
        components: {
          NavBar,
          GameComp,
          FAQBar
        },
  data () {
    return {
      values: [],
      games: myGames,
      allGames: allGames,
      active: false
    }
  },
  
  methods: {
      toggle () {
        this.active = !this.active
      }
      
  },
  created: function () {
    this.$http.get('/api/foos/').then((response) => {
      console.log(response.data)
      this.values = response.data
    })
    console.log("Created")
  },
  addjob: function() {
    myFunction();
  }


};
</script>
