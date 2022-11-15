<script setup>
import Modal from './Modal.vue'
import TaskListItem from './TaskListItem.vue';
import $ from 'jquery'
</script>

<template lang="">
    <div class="draggable-div">
        <h1>{{board_name}}</h1> 
        <draggable class="draggable" ghost-class="ghost-cls" :list="task_list" group="tasks"  item-key="id">
            <TaskListItem v-for="item in task_list" :Name="item.fields.name" :Id="item.pk" @click="ShowModal" @dragend="EndDragging"></TaskListItem>
        </draggable>
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
    props:{
        board_name: String,
        task_list: Array,
    },
    data(){
        return {
            task: this.task_list,
            showModal: false,
        }
    },
    components: {
        Modal,
        draggable: VueDraggableNext,
    },
    methods: {
        ShowModal: function(e){
            this.showModal = true;
            this.itemID = e.target.id;
            console.log(e.target)
        },
        EndDragging: function(e){
            this.emitter.emit("nielsevent", "wallah")
            console.log("STOPPED DRAGGING")
        }
    },
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