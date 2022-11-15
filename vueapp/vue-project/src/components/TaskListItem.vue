<script setup>
defineProps({
  Name: {
    type: String,
    required: true,
  },
  Id: {
    type: Number,
    required: true,
  }
});
</script>

<template lang="">
    <div class="ListItem-div" :id="Id">
    {{Name}}
    </div>
</template>
<script>
export default {
    
}
</script>
<style scoped>
    .ListItem-div{
        width: 100%;
        max-width: 300px;
        background-color: orange;
        border-radius: 5px;
        height: 2rem;
        font-family: sans-serif;
        color: aliceblue;
        display: flex;
        justify-content: center;
        align-items: center;
        margin: 0 auto;
    }
    .ListItem-div:not(:last-child){
        margin-bottom: 1rem;
    }
</style>