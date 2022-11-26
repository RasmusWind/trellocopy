<script setup>
import AddTaskModal from './AddTaskModal.vue'
</script>
<template lang="">
    <div class="bar">
        <button class="add" @click="addclick">Add Task</button>
    </div>
    <Teleport to="body">
      <AddTaskModal :show="showModal" @close="showModal = false"/>
    </Teleport>
</template>
<script>
export default {
    data(){
        return {
            showModal: false,
        }
    },
    props:{
        boarddata:Array,
    },
    components: {
        AddTaskModal,
    },
    methods: {
        addclick: function(event){
            this.showModal = true;
        }
    },
    mounted:function(){
        this.emitter.on("onNewTask", (newTask)=>{
            let board = this.boarddata.filter(b=>{
                return b.pk == newTask.fields.board
            })[0]
            board.fields.tasks.push(newTask)
            board.fields.tasks.sort((a,b) => (a.fields.position > b.fields.position) ? 1 : ((b.fields.position > a.fields.position) ? -1 : 0))
            this.showModal = false
        })
    },
}
</script>
<style scoped>
    .bar {
        display:flex;
        flex-grow: 1;
        height:40px;
        flex-direction: row-reverse;
    }
    .add {
        border-radius: 5px;
        border:none;
        box-shadow: 0 0 4px 0px black;
        margin:5px;
        background-color: rgb(27, 187, 27);
        font-weight: bold;
        color:white;
    }
    button:hover{
        cursor: pointer;
        filter:brightness(110%);
    }
</style>