const axios = require('axios');
require('dotenv').config()

var citasCumplidas = [];

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
    var d = new Date();
    var h = d.getHours();
    var m = d.getMinutes();
    var s = d.getSeconds();
    if (h == 12 && m == 0 && s == 0) {
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
    } else {
        console.log(h + ":" + m + ":" + s);
    }
}, 1000);
