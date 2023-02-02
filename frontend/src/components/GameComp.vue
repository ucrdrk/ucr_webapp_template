<template>
    <div class="modal-backdrop">
      <div class="modal">
        <header class="modal-header">
          <slot name="header">
            Game
          </slot>
        </header>
  
        <section class="modal-body">
          <slot name="body">
            This is the default body!
          </slot>
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
        gamebartype: String
    }
}
</script>
<style>
  .modal-backdrop {
    position: fixed;
    height:261px;
    width:187px;
    background-color: #FFFFFF;
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .modal {
    overflow-x: auto;
    display: flex;
    flex-direction: column;
  }

  .modal-header {
    position: relative;
    font-size: 16px;
    text-align: center;
    top:-10px;

  }
  .modal-footer {
    padding: 15px;
    font-size: 16px;
    text-align: center;
    display: flex;
  }

  .modal-header {
    position:relative;
    text-align: center;
    color: #1A1D1A;
    justify-content: space-between;
  }


  .modal-body {
    position: relative;
    padding: 20px 10px;
  }



  .add-btn {
    color: #FFFFFF;
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