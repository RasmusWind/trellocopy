<script setup>
import Modal from './Modal.vue'
import TaskListItem from './TaskListItem.vue'
import BoardItem from './BoardItem.vue'
import $ from 'jquery'
</script>

<template>

    <div class="HomeBoardList-div">
        <BoardItem v-for="board in boarddata" v-bind:key="board" :board_name="board.fields.name" :task_list="board.fields.tasks"/>
    </div>  
    
  </template>
<script>
import { VueDraggableNext } from "vue-draggable-next"
import get_all_boards_data from "../assets/js/geteverything.js"
import post_boards from "../assets/js/post_delay.js"
var post_timeout = null

export default {
    props:{
        boarddata: Array,
    },
    components: {
        Modal,
        draggable: VueDraggableNext,
    },
    data() {
        return {
            showModal: false,
            drag: false,
            // boarddata:[

            // ],
        }
    },
    methods: {
        ShowModal: function(e){
            this.showModal = true;
            this.itemID = e.target.id;
            console.log(e.target)
        }
    },
    mounted: function(){
        this.emitter.on("nielsevent", (msg)=>{
            // Call delayed post function here!
            post_timeout = post_boards(this.boarddata, post_timeout)
        })
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