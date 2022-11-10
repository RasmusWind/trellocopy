<script setup>
import $ from 'jquery'
</script>

<template lang="">
    <div>
        <form class="createTeam-form" v-on:submit.prevent="submitForm">
            <div>
                <p>Team name:</p>
                <input v-model="form.teamName" placeholder="Team name" />
            </div>
            <div>
                <p>Description:</p>
                <input class="descriptionField" v-model="form.descriptionField" placeholder="Description"/>
            </div>
            <div class="form-group">
                <button class="btn btn-primary">Submit</button>
            </div>
        </form>
    </div>
</template>

<script>
export default {
    data() {
    return {
        form: {
            teamName: "",
            descriptionField: "",
        },
    }
  },
  methods:{
    submitForm(){
        console.log(this.form)
        $.ajax({
            type: "method",
            url: "url",
            data: "data",
            dataType: "dataType",
            success: function (response) {
            }
        });
    }
  },
}
</script>
<style scoped>
    .createTeam-form{
        display: flex;
        background-color: rgb(68, 68, 68);
    }
    .descriptionField{
        width: 300px;
    }
    .createTeam-form div{
        padding: 5px
    }
    .createTeam-form p{
        text-align: center;
        color: aliceblue;
        text-decoration: none;
        font-weight: bold;
        font-family: sans-serif;
    }
    .createTeam-form input{
        height: 1rem;
        border: 0px solid black;
        background-color: darkgray;
        border-radius: 5px;
        padding: 5px;
        color: aliceblue;
        font-family: sans-serif;
    }
</style>