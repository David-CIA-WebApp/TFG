<template>
    <div id="alertas" v-if="logged">
        <div id="menu" v-if="forceReload && logged">
        <button 
        v-if="logged"
        style="background-color: blue; color: white; margin-top: 0px; margin-left: 0px;"
        @click="redirectHome">
            INICIO
        </button>
        <a href="/alertas" class="alertas"><svg viewBox="0 0 15 1" width="32" height="30"><path id="lineBC" d="M 1 1 L 1 2 L 11 2 L 11 1 L 10 0 C 9 -8 3 -8 2 0 L 1 1 M 6 3 A 1 1 0 0 0 6 6 A 1 1 0 0 0 6 3" stroke="black" stroke-width="0.01"  /></svg></a>

        <button 
        v-if="logged"
        style="background-color: transparent; color: red; margin-top: 0px; float: right;"
        @click="closeSession">
            Cerrar Sesión
        </button>
        </div>
        <br>

        <div v-for="alerta in alertas" v-bind:key="alerta">
            <p class="alert" v-if="alerta.activa">
                <p1>
                    {{alerta.descripcion[0]}} 
                    <a v-if="alerta.tipoAlerta=='Inventario'" href="/materials">{{alerta.id_access}}</a> 
                    <a v-if="alerta.tipoAlerta=='Contacto'" href="/consultas">{{alerta.id_access}}</a> 
                    <a v-if="alerta.tipoAlerta=='Revisión'" href="/jobs">{{alerta.id_access}}</a> 
                    {{alerta.descripcion[1]}} 
                </p1>
                <p1 style="position: absolute; right: 300px">{{alerta.fecha}}</p1>
                <p1 style="position: absolute; right: 40px">{{alerta.tipoAlerta}}</p1>
                <input style="position: absolute; right: 20px" type="checkbox" @click="updateAlert(alerta)" checked> 
            </p>
            <p class="alert2" v-if="!alerta.activa">
                <p1>
                    {{alerta.descripcion[0]}} 
                    <a v-if="alerta.tipoAlerta=='Inventario'" href="/materials">{{alerta.id_access}}</a> 
                    <a v-if="alerta.tipoAlerta=='Contacto'" href="/consultas">{{alerta.id_access}}</a> 
                    <a v-if="alerta.tipoAlerta=='Revisión'" href="/jobs">{{alerta.id_access}}</a> 
                    {{alerta.descripcion[1]}} 
                </p1>
                <p1 style="position: absolute; right: 300px">{{alerta.fecha}}</p1>
                <p1 style="position: absolute; right: 40px">{{alerta.tipoAlerta}}</p1>
                <input style="position: absolute; right: 20px" type="checkbox" @click="updateAlert(alerta)" >
            </p>
        </div>
    </div>
</template>

<script>
  import axios from 'axios';

export default {
    data() {
        return {
            logged: false,
            forceReload: false,
            token: null,
            userType: null,
            alertas: []
        }
    },
    methods: {
        updateAlert(alerta) {
            var fechaAEnviar = new Date(alerta.fecha.split('/').reverse().join("-"));
            axios.put(`${process.env.VUE_APP_BACK_URL}/editAlert/`+alerta.id, {
                activa: !alerta.activa,
                fecha: fechaAEnviar.getFullYear() + "-" + (fechaAEnviar.getMonth() + 1) + "-" + fechaAEnviar.getDate()
            }, {
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': this.token
                }
            })
            .then(response => {
                console.log(response);
                this.reloadSite();
            })
            .catch(error => {
                console.log(error);
            });
        },
        loadAlerts() {
            this.alertas = [];
            axios.get(`${process.env.VUE_APP_BACK_URL}/alertas`, {headers:{
                "Content-Type": "application/JSON",
                "Access-Control-Allow-Origin": "*",
                "Authorization": this.token
            }}).then(response => {
                for (let i = 0; i < response.data.length; i++) {
                    var element = response.data[i];
                    element.fecha = new Date(element.fecha);
                    var dia = element.fecha.getDate();
                    if (element.fecha.getMonth() + 1 < 10) {
                        element.fecha = element.fecha.getDate() + "/0" + (element.fecha.getMonth() + 1) + "/" + element.fecha.getFullYear();
                    } else {
                        element.fecha = element.fecha.getDate() + "/" + (element.fecha.getMonth() + 1) + "/" + element.fecha.getFullYear();
                    }
                    if (dia + 1 < 10) {
                        element.fecha = "0/" + element.fecha;
                    }

                    element.descripcion = element.descripcion.split("X");
                    this.alertas.push(element);
                }
                
                this.alertas.sort((a, b) => !a.activa || b.activa && (a.tipoAlerta.localeCompare(b.tipoAlerta) || new Date(b.fecha.split('/').reverse().join("-")) - new Date(a.fecha.split('/').reverse().join("-"))));
            });
        },
        loadData() {
            const path = `${process.env.VUE_APP_BACK_URL}/login`;
            const config = {
                method: 'post',
                url: path,
                data: {
                    "mail": localStorage.userMail, 
                    "password": localStorage.userPass
                },
                headers: {
                    "Content-Type": "application/JSON",
                    "Access-Control-Allow-Origin": "*"
                }
            };
            axios(config)
            .then((res) => {
            if (res.data.accepted) { 
                this.logged = true;
                this.forceReload = true;
                this.userType = localStorage.userType;
                this.token = res.data.token;
                this.loadAlerts();
            }
            
            this.$emit("logging", this.logged);
            })
            .catch((error) => {
            // eslint-disable-next-line
            console.error(error);
            });
        },
        redirectHome() {
            this.$router.push('admin');
        },
        closeSession() {
            localStorage.userMail = "";
            localStorage.userPass = "";
            localStorage.userType = "";
            this.redirectHome();
        },
        reloadSite() {
            this.$router.push('alertas');
            this.$router.go();
        },
    },
      
    mounted() {
        this.loadData();
    }
}
</script>

<style scoped>
.alert {
    background-color: #aaccfd;
    color: rgb(0, 0, 0);
    padding: 15px;
    margin-bottom: 15px;
}
.alert {
    background-color: #d5e7ff;
    color: rgb(0, 0, 0);
    padding: 15px;
    margin-bottom: 15px;
}
</style>