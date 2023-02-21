<template>
    <div class="modal-backdrop">
      <div class="modal">
        <header class="modal-header">
          <slot name="header">
            {{ gameTitle }}
          </slot>
          <div class="platandYear">
            <p class="plat">Platform</p>
            <p class="year">2023</p>
          </div>
        </header>
  
        <section class="modal-body">
          <div class="boxart">boxart here</div>
         </section>
  
        <footer class="modal-footer">
          <button
            type="button"
            class="add-btn"
          >
          Add
          </button>
        </footer>
      </div>
    </div>
</template>
<script>
export default {
    props: {
        gameTitle: String,
        gamePlatform: String,
        releaseYear: Number
    }
}
</script>
<style>
@import url('https://fonts.googleapis.com/css2?family=Inria+Sans&display=swap');
  .modal-backdrop {
    position: fixed;
    height:261px;
    width:187px;
    background-color: #FFFFFF;
    justify-content: center;
    align-items: center;
    border-radius: 15px;
  }

  .modal {
    display: flex;
    flex-direction: column;
  }
  .modal-header {
    font-family: 'Inria Sans', sans-serif;
    position: relative;
    font-size: 16px;
    text-align: center;
    margin-top: 10px;
  }
  .platandYear {
    display: flex;
    flex-direction: row;
    margin-left: 10px;
    margin-top: 10px;
  }
  .plat {
    margin-right: 25px;
  }
  .year{
    margin-left: 25px;
  }

  .modal-footer {

    font-size: 16px;
    text-align: center;
    display: flex;
  }

  .modal-header {
    position:relative;
    text-align: center;
    color: #1A1D1A;

  }

  .modal-body {
    position: relative;
    margin-top: 5px;
    height: 160px;
  }

  .add-btn {
    font-family: 'Inria Sans', sans-serif;
    color: #FFFFFF;
    border: #1A1D1A;
    background-color: #26413C;
    font-size: 20px;
    font-style: bold;
    height:34.68px;
    position: absolute;
    left: 50.86px;
    top: 217px;
    width:84.9px;
  }
</style>