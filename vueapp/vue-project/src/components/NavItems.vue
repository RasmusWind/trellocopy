<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template lang="">
    <div class="NavItems">
        <nav>
            <RouterLink to="/">Home</RouterLink>
            <RouterLink to="/about">About</RouterLink>
            <RouterLink to="/worker">Worker</RouterLink>
            <RouterLink to="/team">Team</RouterLink>
        </nav>

    </div>
</template>
<script>
export default {
    
}
</script>
<style scoped>
    .NavItems nav a{
        color: aliceblue;
        text-decoration: none;
        font-weight: bold;
        font-family: sans-serif;
        width: 60%;
    }    
    .NavItems nav a:not(:first-child){
        padding-left: 1rem;
        border-left: 2px solid #1d3557;
    }    
    .NavItems nav a:not(:last-child){
        padding-right: 1rem;
    }
    .NavItems nav a:hover{
        color: #e63946;
    }
    
    .NavItems{
        margin: 0 auto;
    }

</style>