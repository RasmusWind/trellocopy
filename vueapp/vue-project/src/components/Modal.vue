<script setup>
import TodoItem from './TodoItem.vue'
import vSelect from 'vue-select'
import 'vue-select/dist/vue-select.css';
</script>

<template>
  <Transition name="modal">
    <div v-if="show" class="modal-mask">
      <div class="modal-wrapper" @click="$emit('close')">
        <div class="modal-container" @click.stop="">
            <a class="modal-exit" @click="$emit('close')">X</a>
            <div class="modal-header">
              <div>
            <h1>{{Task.fields.name}}</h1>
          </div>
          <div class="taskDescription-div">
            <button @click="deleteTask" style="background-color:red;">delete</button>
            {{Task.fields.description}}
          </div>
            </div>
          <div class="modal-body">
            <div class="TodoList-div">
                <TodoItem v-for="item in Task.fields.todos" v-bind:key="item" :Name="item.fields.name" :IsComplete="item.fields.complete"/>
            </div>
            <div class="ToolsList-div">
              <div>
                <p>Select Team(s)</p>
                <v-select class="createrWorker-vSelect" multiple @change="AddWorker" v-model="testString" :reduce="(option) => option.id" :options="test" />
            </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </Transition>
</template>

<script >
import { webapi_url } from '../main.js'
import $ from 'jquery'

export default {

  
  props: {
    show: Boolean,
    Task: Object,
    testString: String
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
      ],
      test: [
        {label: "yep", id: 1},
        {label: "nop", id: 2}
      ]
    }
  },
  components: {
    vSelect
  },
  methods:{
    AddWorker(){
      console.log(this)
    },
    deleteTask(){
      let url = `${webapi_url}task-delete/${this.Task.pk}`
      $.ajax({
        type:"delete",
        url:url,
        success:(response)=>{
          this.emitter.emit("onDeleteTask", this.Task)
          this.emitter.emit("onCloseModal")
        }

      })
    }
  },
}
</script>

<style scoped>
    .TodoList-div{
        width: 100%;
        height: 20rem;
        overflow: auto scroll;
        border-right: 2px solid #1d3557;
    }
    .ToolsList-div{
        padding-left: 10px;
        width: 50%;
        height: 20rem;
    }
    .modal-header{
      background-color: #457b9d;
      margin-bottom: 5px;
      padding: 5px 0px;
      border-radius: 10px;
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
        padding-bottom: 2%;
    }

    .modal-container {
        font-family: sans-serif;
        width: 50%;
        margin: 0px auto;
        padding: 5px;
        background-color: #a8dadc;
        color: aliceblue;
        border-radius: 10px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.33);
        transition: all 0.3s ease;
    }
    .modal-container h1{
        border-bottom: 2px solid #1d3557;
        padding-left: 1%;
        padding-bottom: 1rem;
    }
    .modal-footer{
        padding-bottom: 10px;
    }
    .modal-body {
        width: 100%;
        display: flex;
        flex-direction: row;
        background-color: #457b9d;
        border-radius: 10px;
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
    :root {
    --vs-colors--lightest: rgba(60, 60, 60, 0.26);
    --vs-colors--light: rgba(60, 60, 60, 0.5);
    --vs-colors--dark: #333;
    --vs-colors--darkest: rgba(0, 0, 0, 0.15);

    /* Search Input */
    --vs-search-input-color: inherit;
    --vs-search-input-bg: rgb(255, 255, 255);
    --vs-search-input-placeholder-color: inherit;

    /* Font */
    --vs-font-size: 1rem;
    --vs-line-height: 1.4;

    /* Disabled State */
    --vs-state-disabled-bg: rgb(248, 248, 248);
    --vs-state-disabled-color: var(--vs-colors--light);
    --vs-state-disabled-controls-color: var(--vs-colors--light);
    --vs-state-disabled-cursor: not-allowed;

    /* Borders */
    --vs-border-color: var(--vs-colors--lightest);
    --vs-border-width: 1px;
    --vs-border-style: solid;
    --vs-border-radius: 4px;

    /* Actions: house the component controls */
    --vs-actions-padding: 4px 6px 0 3px;

    /* Component Controls: Clear, Open Indicator */
    --vs-controls-color: var(--vs-colors--light);
    --vs-controls-size: 1;
    --vs-controls--deselect-text-shadow: 0 1px 0 #fff;

    /* Selected */
    --vs-selected-bg: #1d3557;
    --vs-selected-color: aliceblue;
    --vs-selected-border-color: var(--vs-border-color);
    --vs-selected-border-style: var(--vs-border-style);
    --vs-selected-border-width: var(--vs-border-width);

    /* Dropdown */
    --vs-dropdown-bg: #1d3557;
    --vs-dropdown-color: inherit;
    --vs-dropdown-z-index: 1000;
    --vs-dropdown-min-width: 160px;
    --vs-dropdown-max-height: 350px;
    --vs-dropdown-box-shadow: 0px 3px 6px 0px var(--vs-colors--darkest);

    /* Options */
    --vs-dropdown-option-bg: #000;
    --vs-dropdown-option-color: var(--vs-dropdown-color);
    --vs-dropdown-option-padding: 3px 20px;

    /* Active State */
    --vs-dropdown-option--active-bg: #5897fb;
    --vs-dropdown-option--active-color: #fff;

    /* Deselect State */
    --vs-dropdown-option--deselect-bg: #fb5858;
    --vs-dropdown-option--deselect-color: #fff;

    /* Transitions */
    --vs-transition-timing-function: cubic-bezier(1, -0.115, 0.975, 0.855);
    --vs-transition-duration: 150ms;
}
</style>