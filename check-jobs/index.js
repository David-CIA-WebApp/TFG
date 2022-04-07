const axios = require('axios');

var trabajos = [];
const path = `${process.env.VUE_APP_BACK_URL}/trabajos`;
const config = {
    method: 'get',
    url: path,
    headers: {
        "Content-Type": "application/JSON",
        "Access-Control-Allow-Origin": "*",
        "Authorization": this.token
    }
}
axios(config).then((res) => {
    for (let index = 0; index < res.data.length; index++) {
        var element = res.data[index];
        trabajos[index] = element;
    }
    setInterval(function(){
        var d = new Date();
        var h = d.getHours();
        var m = d.getMinutes();
        var s = d.getSeconds();
        if (h == 12 && m == 17 && s == 0) {
            console.log(trabajos);
        } else {
            console.log(h + ":" + m + ":" + s);
        }
    }, 1000);
});

