import $ from "jquery"
import {toRaw} from 'vue'
import { webapi_url } from '../../main.js'
function post_boards(board_list, timeout=null){
    if(timeout){
        clearTimeout(timeout)
    }
    console.log("nu laver vi en timeout")
    // Reorder position prop on tasks and todos

    let new_timeout = setTimeout(()=>{
        console.log("Vi poster nu!")
        let url = `${webapi_url}postallboards/`
        $.ajax({
            type:"POST",
            url:url,
            data:{
                data_list:JSON.stringify(toRaw(board_list)),
            },
            error:(err)=>{
                console.error(err)
            }
        })
    }, 2000)

    return new_timeout
}

export default post_boards