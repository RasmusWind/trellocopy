<script setup>
import TodoItem from './TodoItem.vue'

</script>

<template>
  <Transition name="modal">
    <div v-if="show" class="modal-mask">
      <div class="modal-wrapper" @click="$emit('close')">
        <div class="modal-container" @click.stop="">
            <a class="modal-exit" @click="$emit('close')">X</a>
          <div>
            <h1>Placeholder<!-- {{Name}} --></h1>
          </div>
          <div class="taskDescription-div">
            Jeg elsker kage fordi det er nice og jeg elsker det fordi det er lækkert
          </div>

          <div class="modal-body">
            <div class="TodoList-div">
                <TodoItem v-for="item in todos" :Name="item.name" :IsComplete="item.isComplete"/>
            </div>
            <div class="ToolsList-div">
                
            </div>
          </div>

          <div class="modal-footer">
          </div>
        </div>
      </div>
    </div>
  </Transition>
</template>

<script >

export default {
  props: {
    show: Boolean,
    itemID: String
  },
  data(){
    return{
      todos: [
        {name: "Make coffee", isComplete: false},
        {name: "Code css", isComplete: false},
        {name: "Make design", isComplete: true},
        {name: "Code backend", isComplete: true},
        {name: "Go home", isComplete: false},
        {name: "Talk games", isComplete: true},
      ],
      teams: [
        {name: "Backend Developers", Workers: [
          {firstName: "Lars"},
          {firstName: "Jonas"},
          {firstName: "Japa"},
        ]}
      ]
    }
  }
}
</script>

<style>
    .TodoList-div{
        background-color: rgb(34, 144, 247);
        width: 100%;
        height: 20rem;
        overflow: auto scroll;
    }
    .ToolsList-div{
        background-color: #fff;
        width: 50%;
        height: 20rem;
    }
    .modal-mask {
        position: fixed;
        z-index: 9998;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, 0.5);
        display: table;
        transition: opacity 0.3s ease;
    }

    .modal-wrapper {
        display: table-cell;
        vertical-align: middle;
    }
    .taskDescription-div{
        width: 50%;
        padding-left: 2%;
    }

    .modal-container {
        font-family: sans-serif;
        width: 50%;
        margin: 0px auto;
        padding: 20px 30px;
        background-color: rgb(112, 112, 112);
        color: aliceblue;
        border-radius: 5px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.33);
        transition: all 0.3s ease;
    }
    .modal-container h1{
        border-bottom: 2px solid rgb(68, 68, 68);
        padding-left: 1%;
    }

    .modal-header h3 {
        margin-top: 0;
        background-color: rgb(34, 144, 247);
    }
    .modal-footer{
        padding-bottom: 10px;
    }

    .modal-body {
        margin: 20px 0;
        width: 100%;
        display: flex;
        flex-direction: row;
    }

    .modal-exit {
        float: right;
        color: aliceblue;
    }
    .modal-exit:hover {
        color: black;
        cursor: pointer;
    }
    .modal-default-button:not(:first-child){
        margin-right: 5px;
    }

    .modal-enter-from {
        opacity: 0;
    }

    .modal-leave-to {
        opacity: 0;
    }

    .modal-enter-from .modal-container,
    .modal-leave-to .modal-container {
        -webkit-transform: scale(1.1);
        transform: scale(1.1);
    }
</style>