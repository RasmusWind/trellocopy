<script setup>
import Modal from './Modal.vue'
import TaskListItem from './TaskListItem.vue';
</script>

<template>
    <div class="HomeBoardList-div">
        <div class="draggable-div">
            <h1>Icebox</h1> 
            <draggable class="draggable" ghost-class="ghost-cls" :list="list" group="tasks"  item-key="id">
                <TaskListItem v-for="item in list" :Name="item.name" :Id="item.id" v-on:click="ShowModal"></TaskListItem>
            </draggable>
        </div>
        <div class="draggable-div"> 
            <h1>New</h1>      
            <draggable class="draggable" ghost-class="ghost-cls" :list="list2" group="tasks" item-key="id">
                <TaskListItem v-for="item in list2" :Name="item.name" :Id="item.id" v-on:click="ShowModal"></TaskListItem>
            </draggable>
        </div>
        <div class="draggable-div"> 
            <h1>Ongoing</h1>      
            <draggable class="draggable" ghost-class="ghost-cls" :list="list3" group="tasks" item-key="id">
                <TaskListItem v-for="item in list3" :Name="item.name" :Id="item.id" v-on:click="ShowModal"></TaskListItem>
            </draggable>
        </div>
        <div class="draggable-div"> 
            <h1>Done</h1>      
            <draggable class="draggable" ghost-class="ghost-cls" :list="list4" group="tasks" item-key="id">
                <TaskListItem v-for="item in list4" :Name="item.name" :Id="item.id" v-on:click="ShowModal"></TaskListItem>
            </draggable>
        </div>
    </div>  
    <Teleport to="body">
      <!-- use the modal component, pass in the prop -->
      <modal :show="showModal" :itemID="itemID" @close="showModal = false">
        <template #header>
        </template>
      </modal>
    </Teleport>
  </template>
<script>
import { VueDraggableNext } from "vue-draggable-next"
export default {
    
  components: {
    Modal,
    draggable: VueDraggableNext,
  },
  data() {
    return {
      showModal: false,
      drag: false,
      list: [
            {name: "John", id: 1},
            {name: "Kevin", id: 2},
            {name: "Rasmus", id: 3}
        ],      
        list2: [
            {name: "Jacob", id: 4},
            {name: "Japa", id: 5},
            {name: "Jonas", id: 6}
        ],        
        list3: [
            {name: "Lars", id: 7},
            {name: "Karina", id: 8},
            {name: "Rune", id: 9}
        ],        
        list4: [
            {name: "Simon", id: 10},
            {name: "Lærke", id: 11},
            {name: "Frank", id: 12}
        ],
    }
  },
  methods: {
    ShowModal: function(e){
        this.showModal = true;
        this.itemID = e.target.id;
        console.log(e.target)
    }
  }
}
</script>
<style scoped>
    .HomeBoardList-div{
        display: flex;
        flex-wrap: nowrap;
        overflow-x: auto;
        width: 100%;
    }
    .draggable-div{
        border-radius: 10px;
        background-color: rgb(34, 144, 247);
        margin: 3rem;
        width: calc(25% - 6rem);
        flex: 0 0 auto;
        height:0%;
    }    
    .draggable-div h1{
        font-family: sans-serif;
        text-align: center;
        color:aliceblue;
        border-bottom: 2px solid rgb(68, 68, 68);
    }
    .draggable{
        padding: 1rem;
        height: 100%;
    }
    .ghost-cls{
        opacity: 0.3;
        background: rgb(248, 187, 187);
        box-shadow: 2px 2px 8px rgba(0, 0, 0, 1);
    }
</style>