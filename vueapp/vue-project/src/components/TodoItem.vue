<script setup>
defineProps({
  Name: {
    type: String,
    required: true,
  },
  IsComplete: {
    type: Boolean,
    required: true,
  }
});
</script>

<template lang="">
    <div class="TodoItem-div">
        <div class="TodoItemName-div">{{Name}}</div>
        <div class="TodoItemIsComplete-div">{{IsComplete}}</div>
    </div>
</template>
<script>
export default {
}
</script>
<style scoped>
    .TodoItem-div{
        width: calc(100% - 4rem);
        display: flex;
        flex-direction: row;
        padding: 1rem;
        margin: 1rem;
        background-color: darkgray;
        border-radius: 5px;
    }
    .TodoItemIsComplete-div{
        width: 30%
    }
    .TodoItemName-div{
        width: 100%;
        font-family: sans-serif;
    }
    .section::-webkit-scrollbar {
        width: 5px;
    }
</style>