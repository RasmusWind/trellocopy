$.ajax({
    type:"POST",
    url:"hanseland.dk",
    data:{
        "data_list": [
            {
                "boardid":1,
                "position": 0,
                "tasks":[
                    {
                        "taskid":1,
                        "from_boardid":0,
                        "position": 3,
                    },
                    {
                        "taskid":5,
                        "from_boardid":0,
                        "position": 1,
                    },
                    {
                        "taskid":8,
                        "from_boardid":0,
                        "position": 2,
                    },
                    {
                        "taskid":2,
                        "from_boardid":0,
                        "position": 4,
                    },
                ]	
        
            },
            {
                "boardid":3,
                "position": 0,
                "tasks":[
                    {
                        "taskid":7,
                        "from_boardid":4,
                        "position": 3,
                    },
                    {
                        "taskid":1,
                        "from_boardid":1,
                        "position": 3,
                    },
                ]	
        
            },	
        ]

    },

})