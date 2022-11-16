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
        width: calc(100% - 20px);
        max-width: 280px;
        background-color: #1d3557;
        border-radius: 5px;
        height: auto;
        font-family: sans-serif;
        color: aliceblue;
        display: flex;
        justify-content: center;
        align-items: center;
        margin: 0 auto;
        overflow-wrap: break-word;
        padding: 10px;
    }
    .listItem-div:hover{
      color: #e63946;
    }
    .ListItem-div:not(:last-child){
        margin-bottom: 1rem;
    }
</style>