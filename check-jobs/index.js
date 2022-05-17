const axios = require('axios');
require('dotenv').config();

console.log("Checking jobs...\n");

const path = `${process.env.VUE_APP_BACK_URL}/login`;
const config = {
    method: 'post',
    url: path,
    data: {
        "mail": `${process.env.USER}`, 
        "password": `${process.env.PASSWORD}`
    },
    headers: {
        "Content-Type": "application/JSON",
        "Access-Control-Allow-Origin": "*"
    }
};


setInterval(function(){
    axios(config)
    .then((res) => {
        if (res.data.accepted) { 
            const path2 = `${process.env.VUE_APP_BACK_URL}/citasCumplidas`;
            const config2 = {
                method: 'post',
                url: path2,
                headers: {
                    "Content-Type": "application/JSON",
                    "Access-Control-Allow-Origin": "*",
                    "Authorization": res.data.token
                }
            }
            axios(config2).then((res) => {
                console.log(res);
            })
            .catch((err) => {
                console.log("TError:",err);
            });
        }
    })
    .catch((err) => {
        console.log("LError:",err);
    });
}, 86400000);
