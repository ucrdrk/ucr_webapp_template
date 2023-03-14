<template>
    <div class="faqbar">
        <router-link to="/" class="homelink">
            <img src="../assets/logo.png" class="logo">
            <h1 class="title">Cloud2FPGA</h1>
        </router-link>
        <div class="faq">
            <router-link to="/faq"><div v-if="faqbartype ==='home'" class="button">FAQ</div></router-link>
        </div>
    </div>
</template>

<script>
export default {
    props: {
        faqbartype: String
    }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Inria+Sans&display=swap');
.catbar {
    display: flex;
    flex: 0 0 64px;
    justify-content: flex-start;
}
.homelink {
    display: flex;
    flex-direction: row;
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
.catalog {
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