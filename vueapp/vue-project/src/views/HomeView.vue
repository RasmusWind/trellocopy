<script setup>
import HomeBoards from "../components/HomeBoards.vue";
import ActionBar from "../components/ActionBar.vue"
</script>

<template>
    <main>
        <ActionBar :boarddata="boarddata"/>
        <HomeBoards :boarddata="boarddata"/>
    </main>
</template>

<script>
import get_all_boards_data from "../assets/js/geteverything.js"
export default {
    data(){
        return {
            boarddata:[

            ]
        }
    },
    mounted: function(){
        this.boarddata = get_all_boards_data()
    },
}
</script>