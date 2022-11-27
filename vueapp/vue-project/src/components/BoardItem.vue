<script setup>
import Modal from './Modal.vue'
import TaskListItem from './TaskListItem.vue';
import $ from 'jquery'
import {toRaw} from 'vue'
</script>

<template lang="">
    <div class="draggable-div">
        <h1>{{board_name}}</h1> 
        <draggable class="draggable" ghost-class="ghost-cls" :list="task_list" group="tasks"  item-key="id">
            <TaskListItem v-for="item in task_list" :Name="item.fields.name" :Id="/* item.fields.board+'-'+ */item.pk" @click="ShowModal" @dragend="EndDragging"></TaskListItem>
        </draggable>
    </div>
    <Teleport to="body">
      <!-- use the modal component, pass in the prop -->
      <modal :show="showModal" :Task="Task" @close="showModal = false"/>
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
            showModal: false,
            Task: {},
        }
    },
    components: {
        Modal,
        draggable: VueDraggableNext,
    },
    methods: {
        ShowModal: function(e){
            this.showModal = true;
            this.Task = toRaw(this.task_list.filter((t)=>{
                return t.pk == e.target.id
            })[0])
            this.itemID = e.target.id;
        },
        EndDragging: function(e){
            this.emitter.emit("nielsevent", "wallah")
        }
    },
    mounted: function(){
        this.emitter.on("onCloseModal", ()=>{
            this.showModal = false
        })
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
        background-color: #457b9d;
        margin: 1rem 3rem 3rem 3rem;
        width: calc(25% - 6rem);
        flex: 0 0 auto;
        height:0%;
        box-shadow: 0 15px 30px 0 rgb(0 0 0 / 11%), 0 5px 15px 0 rgb(0 0 0 / 8%);
    }    
    .draggable-div h1{
        font-family: sans-serif;
        text-align: center;
        color:aliceblue;
        border-bottom: 2px solid #1d3557;
        padding-bottom: 3%;
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