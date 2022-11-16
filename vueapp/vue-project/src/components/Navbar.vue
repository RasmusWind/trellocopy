<script setup>
import NavItems from './NavItems.vue';
</script>

<template lang="">
    <div class="navbar">
        <h1 class="navbar-h1">Opgavestyring</h1>
        <NavItems />
        <h1 class="navbar-temp">LOGIN TEMP</h1>
    </div>
</template>
<script>
export default {
    
}
</script>
<style scoped>
    .navbar{
        top: 0;
        width: calc(100% - 2rem);
        background-color: #457b9d;
        height: 3.5rem;
        display: flex;
        flex-direction: row;
        align-items: center;
        box-shadow: 0 15px 30px 0 rgb(0 0 0 / 11%), 0 5px 15px 0 rgb(0 0 0 / 8%);
        margin-bottom: 2rem;
        padding: 0px 1rem;
    }
    .navbar-h1{
        font-family: sans-serif;
        padding-left: 5px;
        color: white;
        left: 0;
        width: 20%;
    }
    .navbar-temp{
        font-family: sans-serif;
        padding-right: 5px;
        color: white;
        right: 0;
        width: 20%;
        text-align: right;
    }
</style>