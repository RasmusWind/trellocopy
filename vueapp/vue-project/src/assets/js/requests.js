import $ from "jquery"
import { webapi_url } from '../../main.js'

function get_boards(){
    let result = undefined;

    let url = `${webapi_url}geteverything/`

    $.ajax({
        type:"POST",
        url:url,
        data:{},
        success:(response)=>{
            result = response
            result.sort((a,b) => (a.fields.position > b.fields.position) ? 1 : ((b.fields.position > a.fields.position) ? -1 : 0))
        },
        error:(err)=>{
            console.error(err)
        },
        async:false,
    })
    return result;
}

export default get_boards