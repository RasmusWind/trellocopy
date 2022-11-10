<script setup>
import $ from 'jquery'
</script>

<template lang="">
    <div>
        <form class="createtask-form" v-on:submit.prevent="submitForm">
            <div>
                <p>Task name:</p>
                <input v-model="form.taskName" placeholder="Task name" />
            </div>
            <div>
                <p>Description:</p>
                <textarea rows = "5" cols = "60" name="descriptionField" v-model="form.descriptionField">
                    Enter details here...
                </textarea><br>
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
            taskName: "",
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
    .createTask-form{
        display: flex;
        background-color: rgb(68, 68, 68);
    }

    .createTask-form div{
        padding: 5px
    }
    .createTask-form p{
        text-align: center;
        color: aliceblue;
        text-decoration: none;
        font-weight: bold;
        font-family: sans-serif;
    }
    .createTask-form input{
        height: 1rem;
        border: 0px solid black;
        background-color: darkgray;
        border-radius: 5px;
        padding: 5px;
        color: aliceblue;
        font-family: sans-serif;
    }
</style>