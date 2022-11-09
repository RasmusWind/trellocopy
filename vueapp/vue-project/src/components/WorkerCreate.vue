<script setup>
import $ from 'jquery'
import vSelect from 'vue-select'
</script>

<template lang="">
    <div>
        <form class="createWorker-form" v-on:submit.prevent="submitForm">
            <div>
                <p>First name:</p>
                <input v-model="form.firstName" placeholder="First name" />
            </div>
            <div>
                <p>Last name:</p>
                <input v-model="form.lastName" placeholder="Last name" />
            </div>
            <div>
                <p>Email:</p>
                <input v-model="form.email" placeholder="Email" />
            </div>
            <div>
                <p>Phone number:</p>
                <input v-model="form.phoneNumber" placeholder="Phone number" />
            </div>
            <div>
                <p>Team:</p>
                <v-select class="createrWorker-vSelect" taggable multiple v-model="form.selectedTeam" :reduce="(option) => option.id" :options="[{ label: 'YEP', id: 1},{label: 'yeppers', id: 2}]" />
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
            firstName: "",
            lastName: "",
            email: "",
            phoneNumber: "",
            selectedTeam: "",
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
  components: {
    vSelect
  }
}
</script>
<style scoped>
    .createWorker-form{
        display: flex;
        background-color: rgb(68, 68, 68);
    }
    .createWorker-form div{
        padding: 5px
    }
    .createWorker-form p{
        text-align: center;
        color: aliceblue;
        text-decoration: none;
        font-weight: bold;
        font-family: sans-serif;
    }
    .createWorker-form input{
        height: 1rem;
        border: 0px solid black;
        background-color: darkgray;
        border-radius: 5px;
        padding: 5px;
        color: aliceblue;
        font-family: sans-serif;
    }
    .createWorker-select{
        height: 26px;
        width: 189px;
        border: 0px solid black;
        background-color: darkgray;
        border-radius: 5px;
        padding: 5px;
        color: aliceblue;
        font-family: sans-serif;
    }
    .createrWorker-vSelect{
        background-color: white;
    }
</style>