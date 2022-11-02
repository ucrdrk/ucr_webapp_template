<template>
    <div class="navbar">
        <img src="../assets/Untitled_design_1_-removebg-preview.png" class="logo">
        <h1 class="title">Cloud2FPGA</h1>
        <div class="menu">
            <a href=""><div class="button">Get Started</div></a>
        </div>
    </div>
</template>

<style>
@import url('https://fonts.googleapis.com/css2?family=Inria+Sans&display=swap');
.navbar {
    display: flex;
    flex: 0 1 64px;
    justify-content: flex-start;
}
.logo {
    width: 64px;
    height: auto;
}
.title {
    font-size: 24pt;
    font-family: 'Inria Sans', sans-serif;
    margin-top: auto;
    margin-bottom: auto;
    color: #8AB0AB;
}
.menu {
    margin: auto 2rem auto auto;
}
.button {
    width: 130.67px;
    height: 44px;
    border: 3px solid #8AB0AB;
    border-radius: 10px;
    font-family: 'Inria Sans', sans-serif;
    text-align: center;
    font-size: 16pt; 
    color: #8AB0AB;
    line-height: 44px;
    
}
a {
    text-decoration: none;
}
</style>